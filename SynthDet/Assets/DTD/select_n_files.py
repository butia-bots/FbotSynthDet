import os
import sys
import shutil
import random

def copy_random_n_jpg_files(source_folder, destination_folder, n):
    # Get a list of all files in the source folder
    files = os.listdir(source_folder)

    # Filter the list to include only JPG files
    jpg_files = [file for file in files if file.lower().endswith(('.jpg', '.jpeg'))]

    # Shuffle the list of JPG files randomly
    random.shuffle(jpg_files)

    # Copy the first n JPG files from the shuffled list
    for file in jpg_files[:n]:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.copy(source_path, destination_path)

if len(sys.argv) != 4:
    print("Usage: python script.py source_folder destination_folder n")
else:
    source_folder = sys.argv[1]
    destination_folder = sys.argv[2]
    n = int(sys.argv[3])

    copy_random_n_jpg_files(source_folder, destination_folder, n)