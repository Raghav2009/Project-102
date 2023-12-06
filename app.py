import os
import shutil
from_dir = r"C:\Users\Raghav\Desktop\WhiteHat\Python\Project 102"
to_dir = r"C:\Users\Raghav\Desktop\WhiteHat\Python\Project 102\documents"
list_of_files = os.listdir(from_dir)
# print(list_of_files)
for i in list_of_files:
    name, extension = os.path.splitext(i)
    print('Name is',name)
    print('Extension is',extension)
    if(extension == ""):
        continue
    if(extension in [".txt",".doc",".docx",".pdf"]):
        path1 = from_dir + '/' + i
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + i

        if(os.path.exists(path2)):
            print("Moving "+ i + ".....")
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("Moving "+ i + ".....")
            shutil.move(path1,path3)