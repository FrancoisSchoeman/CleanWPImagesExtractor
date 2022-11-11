import os
import shutil

def list_files(src_dir, save_dir):
    for root, dirs, files in os.walk(src_dir):
        for name in files:
            if "x" not in name and name:
                shutil.copy(os.path.join(root, name), save_dir)

src_dir = input("Path To Uploads Folder: ")
save_dir = input("Path To Destination Folder: ")

list_files(src_dir, save_dir)