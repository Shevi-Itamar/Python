import os
import shutil

def Create_a_new_folder(path,folder_name):
    try:
        my_path = os.path.join(path,folder_name)
        os.makedirs(my_path)
        print("The folder created successfully")
    except Exception as e:
        print("An error occurred: "+str(e))



def create_new_file_in_path(path,file_name):
    my_path = os.path.join(path,file_name)
    if os.path.exists(path):
        if not os.path.exists(my_path):
            with open(my_path,'w') as new_file:
                new_file.write("")
                print ("create a new file in path successfully")
    else:
        print("The file was not created")


def write_to_exist_file(path,my_str):
    if os.path.exists(path):
        with open(path,'a')as myFile:
            myFile.write(my_str)
            print("write to file successfully")
    else:
        print('This file was not written')


def copy_content_of_folder(source_path,destination_path):
    if os.path.exists(source_path):
        if os.path.exists(destination_path):
            content_list = os.listdir(source_path)
            for file in content_list:
                source_file_path=os.path.join(source_path,file)
                destination_file_path = os.path.join(destination_path, file)
                if not os.path.exists(destination_file_path):
                    if os.path.isdir(source_file_path):
                        shutil.copytree(source_file_path,destination_file_path)
                    else:
                        shutil.copy(source_file_path,destination_file_path)
            print('The folder copied successfully')
    else:
       print("The folder not copied")

# מאתחל את הגרסה הנוכחית עם כל הקבצים מהפרויקט
def initialize_current_folder(project_path,current_path):
    if os.path.exists(project_path):
        if os.path.exists(current_path):
            list_of_files = os.listdir(project_path)
            for f in list_of_files:
                if f != '.wit':
                    source_file_path = os.path.join(project_path, f)
                    destination_file_path = os.path.join(current_path, f)
                    if not os.path.exists(destination_file_path):
                        if os.path.isdir(source_file_path):
                            shutil.copytree(source_file_path, destination_file_path)
                        else:
                            shutil.copy(source_file_path, destination_file_path)
            print("The folder copied successfully")
    else:
        print("The folder not copied")

# מחליף קבצים חדשים מהADD בקבצים מהCOMMIT ומעביר את הקבצים מהגרסה הנוכחית לקומיט החדש
def replace_files_from_folder(source_path,destination_path):
    if os.path.exists(source_path):
        if os.path.isdir(source_path):
            if os.path.exists(destination_path):
                list_file_name=os.listdir(source_path)
                for file_name in list_file_name:
                    if os.path.exists(os.path.join(destination_path,file_name)):
                        os.remove(os.path.join(destination_path,file_name))
                    shutil.move(os.path.join(source_path,file_name),os.path.join(destination_path,file_name))
                    print("The file was successfully moved")





def delete_folder(path):
    if os.path.exists(path):
        content_list = os.listdir(path)
        for file in content_list:
            if os.path.isdir(os.path.join(path,file)):
                shutil.rmtree(os.path.join(path,file))
            else:
                os.remove(os.path.join(path,file))


def count_directories(path):
    return sum([1 for entry in os.listdir(path) if os.path.isdir(os.path.join(path, entry))])
