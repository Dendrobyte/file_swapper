import os
import os.path
from os import path
from random import randint

# Navigate to the testing directory
# TODO: Prompt a user for a directory
os.chdir(".\\test_dir") 
# The list for original file names
fileList = os.listdir()

# The list for the new file names, so renamedList[0] was named fileList[0]
renamedList = []

# Temporary list to be emptied when renaming files
tempList = []

# Make a temporary list to later be edited
tempList = fileList

# List for the file names that will be replaced, thus being renamed to an integer n
replacedList = []

# Lists for the NAMING_KEY.txt file
oldName = []
newName = []

# Rename every file in fileList so that they can be replaced later
for i in range(len(fileList)):
    # Add the old name for the NAMING_KEY.txt file
    oldName.append(str(fileList[i]))
    os.rename(fileList[i], str(i))
    replacedList.append(i)

# This retrieves the index in fileList for the renamed file
for presentFile in replacedList:
    # Generate a random number within bounds of fileList
    rand = randint(0, len(tempList)-1)
    # Change the name
    os.rename(str(presentFile), str(tempList[rand]))
    # Add the new name for the NAMING_KEY.txt file
    newName.append(str(tempList[rand]))
    # Remove the tempList value so it is not repeated
    tempList.remove(tempList[rand])

# Generate a file with a key explaining the what file has been renamed to what
naming_key = open("NAMING_KEY.txt", "w+")
naming_key.write("ORIGINAL --> NEW\n")
for i in range(len(newName)):
    naming_key.write(str(oldName[i]) +" --> " + str(newName[i]) + "\n")

# Just in case there is confusiong
naming_key.write("\nIn other words, the file on the left has been renamed to the file on the right.\n")
naming_key.close()
print("Operation File Swap has been a complete success!")