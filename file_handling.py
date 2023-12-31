import os

path = "C:\\Users\\victo\\Desktop\\Victor\\Estudos\\Python\\test.txt"

# File/Dir detection
if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")
print()

# Reading a file
try:
    with open('test.txt', encoding="UTF-8") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")

# Writing a file
text = "\nAdding a new line to file"
try:
    with open('test.txt', 'a', encoding="UTF-8") as file:
        file.write(text)
except FileNotFoundError:
    print("That file was not found :(")

# copyfile() =  copies contents of a file
# copy() =      copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata (file’s creation and modification times)

import shutil

shutil.copyfile('test.txt','copy.txt') #src,dst
# shutil.copyfile('test.txt',"C:\\Users\\User\\Desktop\\test.txt") #src,dst

# moving file/dir
source = "test.txt"
destination = "C:\\Users\\User\\Desktop\\destination.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")

# deleting file/dir
path = "test.txt"

try:
    os.remove(path)    #delete a file
    #os.rmdir(path)     #delete an empty directory
    #shutil.rmtree(path)#delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")