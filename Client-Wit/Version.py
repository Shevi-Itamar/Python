from datetime import datetime
from Modul import create_new_file_in_path, write_to_exist_file, Create_a_new_folder
import os.path
class Version:

    # יוצר גרסה של קומיט חדשה שכוללת יצירת תיקיה וקובץ עם הודעה
    def __init__(self,path,name,message):
        self.name=name
        self.message=message+f"\t {datetime.now().strftime('%d-%m-%y - %H-%M-%S')}"
        self.dir_path=os.path.join(path,name)
        if not os.path.exists(self.dir_path):
            Create_a_new_folder(path,name)
        create_new_file_in_path(self.dir_path,'details')
        file_path=os.path.join(self.dir_path, 'details')
        write_to_exist_file(file_path,self.message+"\t")
