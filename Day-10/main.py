import os

folders=input("Enter folder names with spaces between: ").split(" ")

for folder in folders:
    try:
        files=os.listdir(folder)
    except FileNotFoundError:
        print("Enter valid folder name")
        continue

    print("Files Present in the " + folder + " were =====")
    for file in files:
        print(file)