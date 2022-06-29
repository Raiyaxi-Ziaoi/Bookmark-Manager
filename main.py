import os
import webbrowser
from sys import platform

folderName= "bookmarks.txt"

def delete():
    while True:
        print("\nAre you sure you want to delete all bookmarks? (Y / N):")
        yn = input()
        if yn.lower() == "y":
            os.remove(folderName)
            open(folderName, "x")
            break
        elif yn.lower() == "n":
            break
        else:
            print("\nPlease enter valid input")


def leave():  # Exits program
    print("\nThank you for using Bookmark Manager")
    pause = input("\nPress enter to continue...")
    exit()


def write():  # Writing new bookmarks to file
    try:
        with open(folderName, "a") as f:
            label = input("\nPlease input label for bookmark: ")
            url = input("\nPlease input URL for bookmark: ")
            if os.stat(folderName).st_size == 0:
                f.write(f"{label},{url}")
            else:
                f.write(f"\n{label},{url}")
    except FileNotFoundError:
        open(folderName, "x")
        write()


def bookmarks():  # Display existing bookmarks
    try:        
        with open(folderName, "r") as f:
            print()
            if os.stat(folderName).st_size == 0:
                pause = input("\nThe folder is empty. Please press enter to return to menu.")
                choose()
            else:
                text = f.read()
                text = text.split("\n")

                i = 1
                ulist = []
                for item in text:
                    item = item.split(",")
                    if i < 10:
                        print(f"0{i}. {item[0]}")
                    else:
                        print(f"{i}. {item[0]}")
                    ulist.append(item[1].split("\n"))
                    i += 1
                while True:
                    exceptionPass = True
                    choice = input("\nEnter bookmark to open: ")
                    try:
                        choice = int(choice)
                    except Exception:
                        exceptionPass = False
                    if exceptionPass and choice - 1 <= len(ulist) and choice - 1 >= 0:
                        webbrowser.open(ulist[choice - 1][0])
                        break
                    else:
                        print("\nPlease enter valid input")
    except FileNotFoundError:
        open(folderName, "x")
        bookmarks()

def folderChoose():
    while True:
        folderIn = input("\nWhich folder do you want to open?: ")
        if os.path.exists(folderIn + ".txt"): 
            global folderName
            folderName = folderIn + ".txt"
            break
        else:
            print("\nFolder does not exist")
    choose()

def folder():
    while True:
        folder = input("\nPlease enter folder name: ")
        try: 
            open(folder + ".txt", "x")
            break
        except Exception:
            print("\nFolder already exists.")
    folderChoose()

def displayFolders():
    print()
    file_list = [f for f in os.listdir('.') if os.path.isfile(os.path.join('.', f)) and f.endswith('.txt')]
    i = 1
    for file in file_list:
        file = file.replace(".txt", "")
        if i < 10:
            print(f"0{i}. {file}")
        else:
            print(f"{i}. {file}")

def choose():  # Input validated menu
    print("\nEnter Choice:\n1. Write New Bookmark\n2. Open Bookmarks\n3. Delete All Bookmarks\n4. New Folder\n5. Open Folder\n6. Display All Folders\n7. Exit")
    choice = input()
    if choice == "1":
        write()
        choose()
    elif choice == "2":
        bookmarks()
    elif choice == "3":
        delete()
        choose()
    elif choice == "4":
        folder()
    elif choice == "5":
        folderChoose()
    elif choice == "6":
        displayFolders()
        choose()
    elif choice == "7":
        leave()
        choose()
    else:
        print("\nPlease enter valid input")
        choose()


print("Welcome to Bookmark Manager\n")
choose()
