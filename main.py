# Imports

import os
import webbrowser
from sys import platform

folderName = "Main Bookmarks.txt"


def clearConsole():  # Clears console
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If OS is Win
        command = 'cls'
    os.system(command)


def delete():  # Deletes all bookmarks in a folder
    clearConsole()
    while True:
        print("\nAre you sure you want to delete all bookmarks? (Y / N):")
        yn = input()
        if yn.lower() == "y":
            os.remove(folderName)  # Delete folder
            open(folderName, "x")  # Creates folder
            break
        elif yn.lower() == "n":
            break
        else:
            print("\nPlease enter valid input")
            input("Press enter to continue")
            clearConsole()
    clearConsole()


def leave():  # Exits program
    clearConsole()
    print("\nThank you for using Bookmark Manager")
    input("\nPress enter to continue...")
    exit()


def write():  # Writing new bookmarks to file
    clearConsole()
    try:
        with open(folderName, "a") as f:  # Append to file
            print("\nType back to go back to menu")
            label = input("\nPlease input label for bookmark: ")  # Label
            if label.lower() == "back":  # Go back
                clearConsole()
                choose()
            url = input("\nPlease input URL for bookmark: ")  # URL
            if url.lower() == "back":
                choose()
            if os.stat(folderName).st_size == 0:  # File checks
                f.write(f"{label},{url}")
            else:
                f.write(f"\n{label},{url}")
    except FileNotFoundError:  # File not found
        open(folderName, "x")
        write()


def bookmarks():  # Display existing bookmarks
    clearConsole()
    try:
        with open(folderName, "r") as f:
            print()
            if os.stat(folderName).st_size == 0:
                input("\nThe folder is empty. Please press enter to return to menu.")
                clearConsole()
                choose()
            else:
                text = f.read()
                text = text.split("\n")

                i = 1
                ulist = []  # Bookmark list
                for item in text:
                    item = item.split(",")  # Split and format
                    if i < 10:
                        print(f"0{i}. {item[0]}")
                    else:
                        print(f"{i}. {item[0]}")
                    ulist.append(item[1].split("\n"))
                    i += 1
                print("\nType back to go back to menu.")
                while True:
                    exceptionPass = True
                    choice = input("\nEnter bookmark to open: ")
                    if choice.lower() == "back":
                        break  # Go back
                    try:
                        choice = int(choice)
                    except Exception:
                        exceptionPass = False
                    # Checks
                    if exceptionPass and choice - 1 <= len(ulist) and choice - 1 >= 0:
                        webbrowser.open(ulist[choice - 1][0])  # Open
                        break
                    else:  # Exception not passed
                        print("\nPlease enter valid input")
                        input("Press enter to continue")
                        clearConsole()
    except FileNotFoundError:
        open(folderName, "x")
        bookmarks()


def folderChoose():  # Choose folder to enter
    while True:
        print("\nType back to go back to menu")
        folderIn = input("\nWhich folder do you want to open?: ")
        if folderIn.lower() == "back":
            break  # Go back
        if os.path.exists(folderIn + ".txt"):
            global folderName  # Changes current bookmark folder
            folderName = folderIn + ".txt"
            break
        else:  # Folder does not exist
            print("\nFolder does not exist")
            input("Press enter to continue")
            clearConsole()
    clearConsole()
    choose()


def folder():  # Create folder
    clearConsole()
    while True:
        print("\nType back to go back to menu")
        folder = input("\nPlease enter folder name: ")
        if folder.lower() == "back":  # Go back
            clearConsole()
            choose()
        try:
            open(folder + ".txt", "x")  # Make folder
            break
        except Exception:  # Folder already exists
            print("\nFolder already exists.")
            input("Press enter to continue")
            clearConsole()
    folderChoose()


def displayFolders():  # Display all folders
    clearConsole()
    file_list = [f for f in os.listdir('.') if os.path.isfile(
        os.path.join('.', f)) and f.endswith('.txt')]  # Python list magic
    i = 1
    for file in file_list:  # Display all with formatting
        file = file.replace(".txt", "")
        if i < 10:
            print(f"0{i}. {file}")
        else:
            print(f"{i}. {file}")
        i += 1
    input("\nPress enter to continue...")
    clearConsole()


def remove_empty_lines(filename):  # Python does unusual things if this wasnt here
    if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    with open(filename, "r") as r:
        lines = r.read()
    with open(filename, "w") as w:
        # More Python list magic
        w.write("\n".join([i for i in lines.split('\n') if len(i) > 0]))


def delSpec():  # Delete specific bookmark
    clearConsole()
    try:
        with open(folderName, "r") as f:  # Open folder
            print()
            if os.stat(folderName).st_size == 0:
                input("\nThe folder is empty. Please press enter to return to menu.")
                clearConsole()
                choose()
            else:
                text = f.read()
                text = text.split("\n")

                i = 1
                ulist = []  # Bookmark List
                for item in text:
                    item = item.split(",")
                    if i < 10:
                        print(f"0{i}. {item[0]}")
                    else:
                        print(f"{i}. {item[0]}")
                    ulist.append(item[1].split("\n"))
                    i += 1
                print("\nType back to go back to menu.")
                while True:
                    exceptionPass = True
                    choice = input("\nEnter bookmark to delete: ")
                    if choice.lower() == "back":
                        break
                    try:
                        choice = int(choice)
                    except Exception:
                        exceptionPass = False
                    if exceptionPass and choice - 1 <= len(ulist) and choice - 1 >= 0:
                        try:
                            with open(folderName, 'r') as fr:  # Read to find line to delete
                                lines = fr.readlines()
                                ptr = 1
                                with open(folderName, 'w') as fw:  # Delete line
                                    for line in lines:
                                        if ptr != choice:
                                            fw.write(line)
                                        ptr += 1
                        except:
                            pass
                        break
                    else:
                        print("\nPlease enter valid input")
                        input("Press enter to continue")
                        clearConsole()
    except FileNotFoundError:
        open(folderName, "x")
        bookmarks()


def choose():  # Input validated menu
    remove_empty_lines(folderName)
    print("\nEnter Choice:\n1. Write New Bookmark\n2. Open Bookmarks\n3. Delete All Bookmarks\n4. Delete Specific Bookmark\n5. New Folder\n6. Open Folder\n7. Display All Folders\n8. Exit")
    choice = input()
    match choice:  # New Python feature ftw
        case '1':
            write()
            clearConsole()
            choose()
        case '2':
            bookmarks()
            clearConsole()
            choose()
        case '3':
            delete()
            clearConsole()
            choose()
        case '4':
            delSpec()
            clearConsole()
            choose()
        case '5':
            folder()
        case '6':
            clearConsole()
            folderChoose()
        case '7':
            displayFolders()
            choose()
        case '8':
            leave()
        case other:
            print("\nPlease enter valid input")
            input("Press enter to continue")
            clearConsole()
            choose()


if __name__ == "__main__":  # Main
    os.system('TITLE Register')
    os.system('COLOR 0a')
    print("Welcome to Register\n")
    choose()
