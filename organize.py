import os
import shutil

from_dir = "H:/Python/C102/assets"
to_dir = "H:/Python/C102/Images"

list_of_files = os.listdir(from_dir)
print(list_of_files)

# Move All Files From Assets Folder To Images Folder
for file in list_of_files:
    name,extension = os.path.splitext(file)
    print("Name Of File: ", name)
    print("Extension Of File: ", extension)
    if extension == "":
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        path1 = from_dir + '/' + file
        path2 = to_dir + '/' + 'imagefiles'
        path3 = to_dir + '/' + 'imagefiles' + '/' + file
        print(path1)
        print(path2)
        if os.path.exists(path2):
            print('Moving Files ' + file + "...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print('Moving Files ' + file + "...")
            shutil.move(path1, path3)