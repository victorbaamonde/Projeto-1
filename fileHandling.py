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
