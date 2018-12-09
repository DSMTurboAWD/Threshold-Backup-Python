# Python 3.5.1
import os
import zipfile
import shutil
import time
import random
import shelve
from os.path import normpath
from appJar import gui
import logging

# Global Variables
fromDirectory = ""
toDirectory = ""
fileName = time.time()
fileVersion = str("1.5.11")
logdir = os.path.dirname(__file__)
logFileName = os.path.join(logdir, '/log')
meterHandle = 1

# Setting up the mechanism
def backupsource(btn):
    global fromDirectory
    fromDirectory = app.directoryBox(title="Source")
    app.setStatusbar(fromDirectory, 0)

def backupdest(btn):
    global toDirectory
    toDirectory = app.directoryBox(title="Destination")
    app.setStatusbar(toDirectory, 1)

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(fromDirectory):
        for file in files:
            app.setMeter("progressBar", random.randrange(1, 100), file)
            filePath = os.path.join(root, file)
            ziph.write(filePath, normpath(filePath))

def beginBackup(btn):
    if not app.questionBox("Ready?", "Click to begin backup OK!"):
        app.warningBox("Error", "Cancelled")
    else:
        if (fromDirectory == ""):
            app.warningBox("Error", "No source specified, please check your selection " + fromDirectory)
        elif (toDirectory == ""):
            app.warningBox("Error", "No destination specified, check your selection "
                           + toDirectory)
        else:
            app.infoBox("Title", "Backing up " + fromDirectory + " \nto " + "\n" + toDirectory)
            try:
                zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
                zipdir('temp/', zipf)
                zipf.close()
                shutil.move('Python.zip', toDirectory + "/bak" + str(fileName) + ".zip")
                app.setMeter("progressBar", 100, "Done!")
                app.infoBox("Process Complete", "The Backup Process is complete")
            except Exception as e:
                app.warningBox("Error", "Something went wrong: {}".format(str(e)))
                # logger.error(e)

def closeFunction():
    return app.yesNoBox("Confirm Exit", "Are you sure you want to exit the application?")

# Menu Functions
def aboutback(btn):
    app.infoBox("About", "Version: " + str(fileVersion) + "\nCopyright Threshold Computing, \n2016, \nbuilt 01/09/2016")

def helpFile(btn):
    app.infoBox("Help", "This is a simple backup utility by Threshold Computing. "
                               "\nUse this utility to select a Source and destination directory"
                               " to zip up")

def saveConfig(btn):
    config = shelve.open('config')
    settings = [fromDirectory, toDirectory]
    config['settings'] = settings
    settings.close()

def exitback(btn):
    app.stop()

# Status Functions
def displaysource():
    app.setStatusbar(fromDirectory, 0)

# Open the GUI
app = gui()
app.showSplash("Threshold zip v. " + str(fileVersion), fill="grey", stripe="#ADDFAD", fg="white", font=44)

# Setup the visual styles of the app
app.setTitle("Threshold Zip v. " + str(fileVersion))
app.setIcon("img/logo.ico")
app.setBgImage("img/background.gif")
app.setGeometry(500, 400)
app.setResizable(canResize=True)
app.setPadding([10, 10])
app.setInPadding([5, 5])

# Menu bar

# File Menu
app.createMenu("File", tearable=False)
app.addMenuItem("File", "Save Configuration", func=saveConfig)
app.addMenuItem("File", "Exit", func=exitback, shortcut=None)

# Help Menu
app.createMenu("Help", tearable=False)
app.addMenuItem("Help", "Help", func=helpFile)
app.addMenuItem("Help", "About", func=aboutback, shortcut=None)

# Items inside of the GUI
app.addLabel("title", "Welcome to the simple backup utility", 0, 0, 3)
app.setLabelBg("title", "gray")

# Function Frame
app.startLabelFrame("Backup Utility")
app.setSticky("ew")

# Setup source buttons
app.addLabel("backupsource", "Select a directory to back up: ", 1, 0, 2)
app.addButton("Source", backupsource, 1, 2)
app.setButtonWidth("Source", 10)
app.setLabelBg("backupsource", "#ADDFAD")
app.setLabelWidth("backupsource", 20)
app.setLabelAlign("backupsource", "left")

app.addLabel("backupdest", "Select where to save the backup:", 2, 0, 2)
app.addButton("Destination", backupdest, 2, 2)
app.setButtonWidth("Destination", 10)
app.setLabelBg("backupdest", "#ADDFAD")
app.setLabelWidth("backupdest", 20)
app.setLabelAlign("backupdest", "left")

# Begin Backup section
app.addLabel("backupstart", "Click to begin backup process:", 3, 0, 2)
app.addButton("Backup", beginBackup, 3, 2)
app.setButtonWidth("Backup", 10)
app.setLabelBg("backupstart", "#ADDFAD")
app.setLabelWidth("backupstart", 20)
app.setLabelAlign("backupstart", "left")

# Progress meter
app.addMeter("progressBar", 4, 0, 3)
app.setMeterFill("progressBar", "#ADDFAD")

# End Frame
app.stopLabelFrame()

# Status Bar
app.addStatusbar(fields=2)

# start the GUI
app.go()

# try:
#     global fromDirectory
#     global toDirectory
#     config = shelve.open('config')
#     fromDirectory = config[0]
#     toDirectory = config[1]
# except Exception as f:
#     app.warningBox("Error", "Something went wrong: {}".format(str(f)))