# File version 1.0
# Simply file compression software
# Select directory and compress the contents
# Placing it in a selected location

import os
import shutil
import time
import tkinter as tk
import zipfile
import appJar
from os.path import relpath
from tkinter import filedialog

fileVersion = 1.0
fromDirectory = ""
toDirectory = ""
fileList = []
fileName = time.time()
mainFunc = 0

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(fromDirectory):
        for file in files:
            with Archive.progressbar.progressbar(max_value=10) as progress:
                for i in range(1):
                    filePath = os.path.join(root, file)
                    ziph.write(filePath, relpath(filePath, ""))
                    time.sleep(0.1)
                    progress.update(i)

while (mainFunc == 0):
    print(("Threshold Backup v " + str(fileVersion)).center(58, "_"))
    print("**********************************************************")
    print("")
    print("              Welcome to the file compression")
    print("                  and backup software.")
    print("")
    print("**********************************************************")
    print("")
    print("This function will zip up a directory")
    print("and place the contents in the backup directory")
    print("")
    print("for more information type: '-h'")
    print("To run the default operation type: 'Backup'")
    print("")
    print("----------------------------------------------------------")
    print("")
    prompt = str(input("what would you like to do?"))

    if (prompt.upper() == "BACKUP" or prompt.upper() == "-B"):
        root = tk.Tk()
        root.withdraw()
        print("Would you like to specify a directory to backup?")
        print("")
        promptDir = str(input("Yes or no?"))
        if (promptDir.upper() == "YES" or promptDir.upper() == "Y" ):
            fromDirectory = filedialog.askdirectory(initialdir="./",
                                              title="Select a folder to backup")
        else:
            print("File will copy from the default save location")

        print("Would you like to specify a destination directory?")
        print("")
        promptDir = str(input("Yes or no?"))
        if (promptDir.upper() == "YES" or promptDir.upper() == "Y"):
            toDirectory = filedialog.askdirectory(initialdir="./",
                                                  title="Select a destination directory")
        else:
            print("Will save to the default directory")

        print("")
        print("Ready to backup")
        endFunc = input("Press Enter to Continue...")
        zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
        zipdir('tmp/', zipf)
        zipf.close()
        os.renames('Python.zip', "bak" + str(fileName) + ".zip")
        shutil.move("bak" + str(fileName) + ".zip", str(toDirectory) + "/bak" + str(fileName) + ".zip")
        print("***Process complete***")
        mainFunc = 1

    elif (prompt == "-h" or prompt.upper() == "HELP"):
        print(("Help File v " + str(fileVersion)).center(58, "_"))
        print("**********************************************************")
        print("")
        print("-b or 'backup' will prompt to select a folder location")
        print("-h or 'help' will show this message")
        print("-v or 'version' will display version information")
        print("-q or 'quit' will exit this program")
        print("")
        print("**********************************************************")
        endFunc = input("Press any key to continue...")
        mainFunc = 0

    elif (prompt == "-v" or prompt.upper() == "VERSION"):
        print(str(fileVersion))
        promptRec = input("Press enter to continue...")
        mainFunc = 0

    elif (prompt == "-q" or prompt.upper() == "QUIT"):
        break

    else:
        print("I did not understand what you want to do")
        endFunc = input("Press any key to continue")
        mainFunc = 0
