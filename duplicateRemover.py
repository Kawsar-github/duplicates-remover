
import os
import shutil
import hashlib
from collections import defaultdict

def get_file_hash(filename):
    """Return the MD5 hash of a given file."""
    hasher = hashlib.md5()
    with open(filename, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()


def remove_duplicate_files(directory):
    """Remove duplicate files in a directory and its subdirectories."""
    unique_hashes_to_paths = defaultdict(list)  # Map hash to list of paths
    
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            print(filename[0:15],"...            ",filename[-4::],"               ",end="\r")
            file_hash = get_file_hash(filepath)
            
            # Append path to list if hash is new or the paths are not identical
            
            unique_hashes_to_paths[file_hash].append(filepath)
        
    dup_number=0
    for file_list in unique_hashes_to_paths.values():
        if len(file_list) > 1:
            for dfiles in file_list:
                print("Duplicate found: ",dfiles,end="\n")
                dup_number=dup_number+1
            print("####->\nOnly ",file_list[-1]," will be kept",end="\n####\n\n") 
            dup_number=dup_number-1
    print(dup_number," DUPLICATES FOUND!!",end="\n")
    if dup_number>0:
        term=input("Do you want to remove this duplicats?(Y/n): ")
        if term.lower()=="y":
            for file_listx in unique_hashes_to_paths.values():
                at=0
                if len(file_listx) > 1:
                    for _ in range(len(file_listx) - 1):
                        print("Removing: ",file_listx[at])
                        os.remove(file_listx[at])
                        at=at+1
            print("DUPLICATES REMOVED!")
        else:
            print("Aborted!!")
    else:
        print("NO DUPLICATES FOUND!") 

   

if __name__ == "__main__":
    dir= input("Please give the file path to remove duplicate(e.g. /home/linux/Downloads/): ")
    if not dir.endswith("/"):
        dir=dir+"/"
    if not os.path.exists(dir):
        print("The following path doesn't exsists...")
    else:
        print("Path found! Scanning for duplicates...\n")
        remove_duplicate_files(dir)
    