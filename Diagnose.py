#name, path, size
import os
import time
from tabulate import tabulate

all_files = []
all_folders = []
def check_files_folders(current_path):
    # print(f"Current path: {current_path}", end='\r')
    file_list = os.listdir(current_path)
    folder_name = current_path[-1*current_path[:-1][::-1].find('\\')-1:-1]
    folder_path = current_path
    folder_size = 0

    for file_ in file_list:
        if os.path.isdir(current_path + file_) == True:
            try:
                temp = check_files_folders(current_path + file_ + '\\')
                folder_size += temp
            except:
                continue

        else:
            try:
                file_name = file_
                file_path = current_path + file_
                file_size = os.stat(file_path).st_size//(1024*1024)
                folder_size += file_size
                all_files.append([file_name, file_path, file_size])
            except:
                continue

    all_folders.append([folder_name, folder_path, folder_size])
    return folder_size

drive_letters = [i.upper() for i in input("Enter The Drive Letter(C, D, E ...) to scan (If multiple keep them space separated): ").split()]

total_size = 0
for drive_letter in drive_letters:
    time.sleep(1)
    print(f"\nStarting Diagnosing Drive {drive_letter}..........\n")
    if drive_letter == 'C':
        root_path = u"\\\\?\\C:\\"    #Root path for C Drive
    else:
        root_path = drive_letter+":\\" 
    total_size += check_files_folders(root_path)
    print(f"\nEnding Diagnosing Drive {drive_letter}..........\n")

all_files = sorted(all_files, key=lambda x: x[2], reverse=True)
all_folders = sorted(all_folders, key=lambda x: x[2], reverse=True)
files_folders = [i+["File"] for i in all_files]
files_folders = files_folders + [i+["Folder"] for i in all_folders]

files_folders = sorted(files_folders, key=lambda x: x[2], reverse=True)

all_files = [[i[0], i[1], str(i[2])+ " MB"] for i in all_files]
all_folders = [[i[0], i[1], str(i[2])+ " MB"] for i in all_folders]
files_folders = [[i[0], i[1], str(i[2])+ " MB", i[3]] for i in files_folders]

time.sleep(1)
print("\n")
print(f"Total number of files excluding folders: {len(all_files)}")
print(f"Total number of Folders: {len(all_folders)}")
print(f"Total files and folders: {len(all_files) + len(all_folders)}")
print(f"Total Size of root directory: {total_size}")

while True:

    choice = int(input("1: Inspect Folders 2: Inspect Files 3: Inspect all files and Folders::      "))

    if choice == 1:
        index = 0
        while(index < len(all_folders)):
            more = input("Press Enter to see another 5 entries\n")
            data = all_folders[index:index+5]
            print(tabulate(data, headers=["Folder Name", "Folder Path", "Folder Size"], tablefmt='orgtbl'))
            index += 5

    elif choice == 2:
        index = 0
        while(index < len(all_files)):
            more = input("Press Enter to see another 5 entries\n")
            data = all_files[index:index+5]
            print(tabulate(data, headers=["File Name", "File Path", "File Size"], tablefmt='orgtbl'))            
            index += 5

    else:
        index = 0
        while(index < len(files_folders)):
            more = input("Press Enter to see another 5 entries\n")

            data = files_folders[index:index+5]
            print(tabulate(data, headers=["Name", "Path", "Size", "Type"], tablefmt='orgtbl'))
            index += 5
