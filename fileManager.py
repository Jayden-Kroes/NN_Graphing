import os
import random

def random_name(length=10):
    characters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    name=""
    for i in range(length):
        name +=characters[random.randint(0, len(characters)-1)]
    return name

def get_random_directory(parent_directory=None, ensure_random=True):
    dirName = random_name()
 
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ") 
        return dirName
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")
        if ensure_random:
            return get_random_directory(parent_directory=parent_directory, ensure_random=True)
        else:
            return dirName
