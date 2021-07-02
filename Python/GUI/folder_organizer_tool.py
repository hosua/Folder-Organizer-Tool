from colorama import Fore, Back, Style
import os
import shutil
import string
from tkinter import messagebox
import string

colored = False
fg_prompt = Fore.LIGHTCYAN_EX
fg_good = Fore.GREEN
fg_error = Fore.RED
fg_reset = Fore.RESET
if not colored:
    fg_prompt = ""
    fg_good = ""
    fg_error = ""
    fg_reset = ""


# Lot's of testing needs to be done before releasing this. Extract extras is also incomplete right now.

def extractSubStr(dir, subStr):
    try:
        os.chdir(dir)
    except FileNotFoundError:
        print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
        return ""
    new_dir = os.path.join(dir, subStr.upper())
    if not os.path.exists(new_dir):
        print(fg_good + "Created directory " + new_dir + fg_reset)
        os.makedirs(subStr)
    for item in os.listdir(dir):
        if os.path.isfile(item):    # make sure were working with a file
            if item.lower().__contains__(subStr.lower()):
                try:
                    print(fg_good + "Moving " + fg_prompt + item +
                          fg_good + " to " + fg_prompt + new_dir + fg_reset)
                    shutil.move(item, new_dir)
                except shutil.Error:
                    print("Detected duplicate item: " + item + " in " + new_dir)
                    isOverwriting = messagebox.askyesno("Question", "A duplicate of " + item + " was found in " + new_dir+ ". Do you want to overwrite it?")
                    if isOverwriting:
                        try:                        
                            print("Copying " + item + " to " + new_dir)
                            shutil.copy(item, new_dir)  # Copying will either create or overwrite
                        except shutil.SameFileError:
                            pass    # unless they're exactly the same
                        print("Removing " + item + " from " + dir)
                        os.remove(item)
                    else:
                        print("Ignoring " +item + " in " + dir)
    print(fg_good + "Process completed...\n\n" + fg_reset)


def keepSubStr(dir, subStr):
    if not dir == "":
        try:
            os.chdir(dir)
        except FileNotFoundError:
            print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
            return ""
    else:
        try:
            os.chdir(dir)
        except FileNotFoundError and OSError:
            print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
            return ""

    extr = "Extracted"
    new_dir = os.path.join(dir, extr)
    if not os.path.exists(new_dir):
        print(fg_good + "Created directory " + new_dir + fg_reset)
        os.makedirs(extr)
    for item in os.listdir(dir):
        if os.path.isfile(item):    # make sure were working with a file
            if not subStr.lower() in item.lower():
                try:
                    print(fg_good + "Moving " + fg_prompt + item +
                          fg_good + " to " + fg_prompt + new_dir + fg_reset)
                    shutil.move(item, new_dir)
                except shutil.Error:
                    print("Detected duplicate item: " + item + " in " + new_dir)
                    isOverwriting = messagebox.askyesno("Question", "A duplicate of " + item + 
                                " was found in " + new_dir + ". Do you want to overwrite it?")
                    if isOverwriting:
                        print("Copying " + item + " to " + new_dir)
                        shutil.copy(item, new_dir)  # Copying will either create or overwrite, no matter what.
                        print("Removing " + item + " from " + dir)
                        os.remove(item)
                    else:
                        print("Ignoring " + item + " in " + dir)
                    continue
    print(fg_good + "Process completed with no errors...\n\n" + fg_reset)
    return dir


def extractAllFolders(dir):
    try:
        os.chdir(dir)
    except FileNotFoundError:
        print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
        return ""

    for item in os.listdir(dir):
        new_path = os.path.join(dir, item)
        if os.path.isdir(new_path):  # ensure were not a file
            for file in os.listdir(new_path):   # File isn't just files, but also dirs.
                filePath = os.path.join(new_path, file)
                try:
                    print(fg_good + "Moving " + fg_prompt + file +
                        fg_good + " to " + fg_prompt + dir + fg_reset)
                    shutil.move(filePath, dir)
                except shutil.Error:
                    print("Detected duplicate item " + file + " in " + dir)
                    isOverwriting = messagebox.askyesno("Warning", "A duplicate of " + file + 
                                " was found in " + dir + ". Do you want to overwrite it?")
                    if isOverwriting:
                        print("Copying " + file + " to " + dir)
                        try:
                            shutil.copy(filePath, dir)  # Copying will overwrite unless files are exactly the same.
                        except shutil.SameFileError:    # Just pass in this case.
                            pass
                        print("Removing " + os.path.basename(filePath) + " from " + filePath)
                        os.remove(filePath)
                    else:
                        print("Ignoring " + os.path.basename(filePath) + " in " + filePath)
                    continue
    for item in os.listdir(dir):
        new_path = os.path.join(dir, item)
        if os.path.isdir(new_path) and len(os.listdir(new_path)) == 0:
            print(fg_error + "Removing " + new_path + " because it was empty." + fg_reset)
            os.rmdir(new_path)
    print(fg_good + "Process completed with no errors...\n\n" + fg_reset)
    return dir


def alphabetizeFolders(dir, numLetters=3):
    def getFolderNames():
        folderNames = []
        start = 0
        end = numLetters
        while end < len(string.ascii_uppercase)+1:
            folderNames.append(string.ascii_uppercase[start:end])            
            start += numLetters
            end += numLetters
        currAlpha = ""
        for name in folderNames:
            currAlpha += name
        lastFolder = ""  # Handle any leftover letters
        if currAlpha != string.ascii_uppercase:
            for letter in string.ascii_uppercase:
                if letter not in currAlpha:
                    lastFolder += letter
                    print(lastFolder)
        if lastFolder != "":
            folderNames.append(lastFolder)
        return folderNames

    try:
        os.chdir(dir)
    except FileNotFoundError:
        print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
        return ""

    folderNameList = getFolderNames()   # Get the name list
    folderPathList = []

    for folder in folderNameList:   # Create the directories
        new_dir = os.path.join(dir, folder)
        if not os.path.exists(new_dir):
            print(fg_good + "Created directory " + new_dir + fg_reset)
            os.makedirs(new_dir)
    misc = "#"  # Make the directory for anything that doesn't start with a letter
    misc_dir = os.path.join(dir, misc)
    if not os.path.exists(misc_dir):
        print(fg_good + "Created directory " + misc_dir + fg_reset)
        os.makedirs(misc_dir)

    for item in folderNameList:
        folderPathList.append(os.path.join(dir, item))

    for folder in folderPathList:    # For each alphabetized folder
        new_dir = os.path.join(dir, folder)
        for file in os.listdir(dir):
            if os.path.isfile(file) and file[0].upper() in os.path.basename(folder):
                try:
                    print(fg_good + "Moving " + fg_prompt + file +
                        fg_good + " to " + fg_prompt + new_dir + fg_reset)
                    shutil.move(file, new_dir)
                except shutil.Error:
                    print("Detected duplicate item " + file + " in " + new_dir)
                    isOverwriting = messagebox.askyesno("Question", "A duplicate of " + file + 
                                " was found in " + new_dir + ". Do you want to overwrite it?")
                    if isOverwriting:
                        print("Copying " + file + " to " + new_dir)
                        try:
                            shutil.copy(file, new_dir)  # Copying will overwrite unless files are exactly the same.
                        except shutil.SameFileError:    # Just pass in this case.
                            pass
                        print("Removing " + file + " from " + new_dir)
                        os.remove(file)
                    else:
                        print("Ignoring " + file + " in " + new_dir)

    # move the left over files that didn't get sorted into #
    for file in os.listdir(dir):
        # Ensure we don't grab duplicates that the user didn't overwrite
        if os.path.isfile(file) and not file[0] in string.ascii_letters:   
            try:
                print(fg_good + "Moving " + fg_prompt + file +
                      fg_good + " to " + fg_prompt + misc_dir + fg_reset)
                shutil.move(file, misc_dir)
            except shutil.Error:
                print("Detected duplicate item " + file + " in " + misc_dir)
                isOverwriting = messagebox.askyesno("Question", "A duplicate of " + file + 
                            " was found in " + misc_dir + ". Do you want to overwrite it?")
                if isOverwriting:
                    try:
                        print("Copying " + file + " to " + misc_dir)
                        shutil.copy(file, misc_dir)  # Copying will overwrite unless files are exactly the same.
                    except shutil.SameFileError:    # Just pass in this case.
                        pass
                    print("Removing " + file + " from " + misc_dir)
                    os.remove(file)
                else:
                    print("Ignoring " + file + " in " + misc_dir)

    for item in os.listdir(dir):    # Remove empties
        if os.path.isdir(item) and len(os.listdir(item)) == 0:
            print(fg_error + "Removing " + item + " because it was empty." + fg_reset)
            os.rmdir(item)
    print(fg_good + "Process completed with no errors...\n\n" + fg_reset)
    return dir


# Still need to find a way to omit multi-disc games
def extractDuplicates(dir):  
    try:
        os.chdir(dir)
    except FileNotFoundError or OSError:
        print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
        return ""

    nameList = []
    dupeList = []
    for file in os.listdir(dir):
        if os.path.isfile(file):
            name = file.split("(")[0]
            if name not in nameList:
                nameList.append(name)
            elif name not in dupeList:            
                dupeList.append(name)
    dupe_dir = os.path.join(dir, "Duplicates")
    if not os.path.exists(dupe_dir):
        os.mkdir("Duplicates") 
    for file in os.listdir(dir): # split text to remove file extension            
        for dupe in dupeList: # and get lower-cased title
            title = os.path.splitext(os.path.basename(file))[0].lower().split("(")[0]   
            if title == dupe.lower():               
                try:
                    print(fg_good + "Moving " + fg_prompt + file +
                          fg_good + " to " + fg_prompt + dupe_dir + fg_reset)
                    shutil.move(file, dupe_dir)
                except shutil.Error:
                    print("Detected duplicate item: " + file + " in " + dupe_dir)
                    isOverwriting = messagebox.askyesno("Question", "A duplicate of " + file + 
                                " was found in " + dupe_dir + ". Do you want to overwrite it?")
                    if isOverwriting:
                        print("Copying " + file + " to " + dupe_dir)
                        try:
                            shutil.copy(file, dupe_dir)  # If it can't copy, then the files are exactly identical.
                        except: # So just skip it.
                            pass    
                        print("Removing " + file + " from " + dupe_dir)
                        os.remove(file)
                    else:
                        print("Ignoring " + file + " in " + dupe_dir)
                    continue
    print(fg_good + "Process completed..." + fg_reset + "\n")

def extractExtras(dir):
    try:
        os.chdir(dir)
    except FileNotFoundError:
        print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
        return

    
    ext_dir = os.path.join(dir, "Extras")
    if not os.path.exists(ext_dir):
        print(fg_good + "Created directory " + ext_dir + fg_reset)
        os.makedirs("Extras")

    extrasList = ["(Beta", "Beta)",
                  "(Proto", "Proto)",
                  "(Demo", "Demo)",
                  "(Tech Demo", "Tech Demo)",
                  "(Debug", "Debug)",
                  "(Kiosk", "Kiosk)",
                  "(Sample", "Sample)",
                  "(Aftermarket", "Aftermarket)",
                  "(Unknown", "Unknown)",
                  "(Unl", "Unl)",
                  "(Bootleg", "Bootleg)",
                  "[BIOS", "BIOS]",
                  "(Prerelease", "Prerelease)"]

    # Make all dirs
    clean_tags = [extrasList[i].strip(string.punctuation) for i in range(len(extrasList)) if i % 2 == 0] 
    [os.mkdir(os.path.join(ext_dir, clean_tags[i])) for i in range(len(clean_tags)) if not os.path.exists(ext_dir)]

    for file in os.listdir(dir):
        if os.path.isfile(file):
            for tag in extrasList:
                #print("file:", file, " tag:", tag)
                if file.lower().__contains__(tag.lower()):
                    clean_tag = tag.translate(
                        str.maketrans("", "", string.punctuation))
                    destination = os.path.join(ext_dir, clean_tag)
                    print(destination)
                    if not os.path.isdir(destination):
                        print("making directory " + destination + " for " + file)
                        os.mkdir(destination)
                    try:
                        print(fg_good + "Moving " + fg_prompt + file +
                            fg_good + " to " + fg_prompt + destination + fg_reset)
                        shutil.move(file, destination)
                    except shutil.Error: # if there is another file with the same name
                        print("Detected duplicate file " + file + " in " + destination)
                        isOverwriting = messagebox.askyesno("Question", "A duplicate of " + file + 
                                    " was found in " + destination + ". Do you want to overwrite it?")
                        if isOverwriting:
                            try:
                                print("Copying " + file + " to " + destination)
                                shutil.copy(file, destination)  # Copying will overwrite unless files are exactly the same.
                            except shutil.SameFileError:    # Just pass in this case.
                                pass
                            print("Removing " + file + " from " + destination)
                            os.remove(file)
                        else:
                            print("Ignoring " + file + " in " + destination)
                    break   # Break out of tag once we hit one to avoid double counting
