import os

folders = input("Enter the folders").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print(folder+" is not a valid folder")
        continue
    print("Files in the folder " + folder+": ")
    for file in files:
        print(file)