import os
import shutil
from Version import Version
from Modul import Create_a_new_folder, copy_content_of_folder, replace_files_from_folder, delete_folder,initialize_current_folder,count_directories
import json
import webbrowser
import requests
from colorama import Fore, Style, init
from colorama import init
init(autoreset=True)


class repository:
    def __init__(self):
        path = os.path.join(os.getcwd(), '.wit')
        if not os.path.exists(os.path.join(path, 'staging')):
            Create_a_new_folder(path, 'staging')
        if not os.path.exists(os.path.join(path, 'commiting')):
            Create_a_new_folder(path, 'commiting')
        if not os.path.exists(os.path.join(path, 'current version')):
             current_version=Version(path, 'current_version', 'first version')
        self.path_commiting=os.path.join(path,'commiting')
        self.path_staging=os.path.join(path, 'staging')
        self.path_current_version=os.path.join(path, 'current_version')
        initialize_current_folder(os.getcwd(),self.path_current_version)


    def add(self,file_name):
       path=os.path.join(os.getcwd(),file_name)
       if os.path.exists(path):
            if os.path.isfile(path):
                shutil.copy(path, self.path_staging)
                print('The file added successfully')
       else:
            print('This path is not file')


    def commit(self,message):
        if os.listdir(self.path_staging):
            count_commit=count_directories(self.path_commiting)
            name = str(count_commit+1)
            new_version=Version(self.path_commiting,name,message)
            copy_content_of_folder(self.path_current_version,new_version.dir_path)
            replace_files_from_folder(self.path_staging,new_version.dir_path)
            delete_folder(self.path_current_version)
            copy_content_of_folder(new_version.dir_path,self.path_current_version)
            print('The version commiting successfully')
        else:
            print('The staging is empty')


    def log(self):
        list_files=os.listdir(self.path_commiting)
        for commit_name in list_files:
            print("Commit name: "+commit_name)
            my_commit_path=os.path.join(self.path_commiting,commit_name)
            my_detail_path=os.path.join(my_commit_path,'details')
            with open(my_detail_path ,'r')as my_file:
                print("message: "+my_file.readline())


    def status(self):
        if os.listdir(self.path_staging):
            print('You can make commit')
        else:
            print('The staging is empty')



    def checkout(self,commit_id):
        my_path=os.path.join(self.path_commiting,commit_id)
        if os.path.exists(my_path):
            delete_folder(self.path_current_version)
            copy_content_of_folder(my_path,self.path_current_version)
            print('')
        else:
            print('The commit does not exists')

    def push(self):
        url = 'http://localhost:8000/'
        print(">> Starting push...")
        folders = [f for f in os.listdir(self.path_commiting) if os.path.isdir(os.path.join(self.path_commiting, f))]
        if not folders:
            print(Fore.RED + "No folders found in the commiting path")
            return

        folders = sorted(folders, key=lambda f: os.path.getmtime(os.path.join(self.path_commiting, f)))
        last_commit = folders[-1]

        folder_to_zip = os.path.join(self.path_commiting, last_commit)
        zip_base = folder_to_zip  # בסיס שם הקובץ בלי סיומת
        zip_path = zip_base + '.zip'

        shutil.make_archive(base_name=zip_base, format='zip', root_dir=folder_to_zip)
        print("Creating zip from:", folder_to_zip)
        print("Zip path:", zip_path)
        try:
            with open(zip_path, 'rb') as file:
                files = {'file': ('MyFolder.zip', file, 'application/zip')}
                print("Sending alert request to:", url + 'alert')
                alert_resp = requests.post(url + 'alert', files=files)
                if alert_resp.status_code == 200:
                    alert_data = alert_resp.json()
                    print(Fore.GREEN + "Alert response:")
                    print(Fore.GREEN + json.dumps(alert_data, indent=4, ensure_ascii=False))
                else:
                    print(Fore.RED + f"Alert request failed: {alert_resp.status_code}")

                file.seek(0)
                files = {'file': ('MyFolder.zip', file, 'application/zip')}

                graphs_resp = requests.post(url + 'analyze', files=files)
                if graphs_resp.status_code == 200:
                    paths = graphs_resp.json()
                    print(Fore.CYAN + "\nOpening graph images...")
                    for path in paths:
                        webbrowser.open(path)
                else:
                    print(Fore.RED + f"Graphs request failed: {graphs_resp.status_code}")

        except Exception as e:
            print(Fore.RED + f"An error occurred: {str(e)}")