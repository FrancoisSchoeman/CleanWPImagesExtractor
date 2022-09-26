import os
import shutil

def list_files(src_dir, save_dir):
    for root, dirs, files in os.walk(src_dir):
        for name in files:
            if "x" not in name:
                shutil.copy(os.path.join(root, name), save_dir)

src_dir = input("Source Folder, eg: 'C:\Users\Path\To\Uploads\Folder': ")
save_dir = input("Destination Folder, eg: 'C:\Users\Path\To\Destination\Folder': ")

list_files(src_dir, save_dir)