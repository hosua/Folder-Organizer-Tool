from colorama import Fore, Back, Style
import os
import shutil
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
                    print(fg_good + "The file " + fg_prompt + item + fg_good +
                          " was already in " + fg_prompt + new_dir + fg_reset + " !")
                    print(
                        fg_good + "I will skip this item but you will have to manage these files yourself!" + fg_reset)
                    continue

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
                    print("Skipped a duplicate file")
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
        if os.path.isdir(new_path):  # if new_item is a dir
            for file in os.listdir(new_path):
                filePath = os.path.join(new_path, file)
                print(fg_good + "Moving " + fg_prompt + file +
                      fg_good + " to " + fg_prompt + dir + fg_reset)
                try:
                    shutil.move(filePath, dir)  # move file to root dir
                except shutil.Error:
                    print("Could not move a file because it was a duplicate")

    for item in os.listdir(dir):
        new_path = os.path.join(dir, item)
        if os.path.isdir(new_path) and len(os.listdir(new_path)) == 0:
            print(fg_error + "Removing " + new_path + fg_reset)
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

    for file in os.listdir(dir):    # sort each file into the folders we created
        if os.path.isfile(file):
            for folder in folderPathList:
                new_dir = os.path.join(dir, folder)
                if file[0].upper() in os.path.basename(folder):
                    try:
                        print(fg_good + "Moving " + fg_prompt + file +
                              fg_good + " to " + fg_prompt + folder + fg_reset)
                        shutil.move(file, new_dir)
                    except shutil.SameFileError:
                        print("Skipping file because it was a duplicate")

    # move the left over filse that didn't get sorted into #
    for file in os.listdir(dir):
        if os.path.isfile(file):
            try:
                print(fg_good + "Moving " + fg_prompt + file +
                      fg_good + " to " + fg_prompt + misc_dir + fg_reset)
                shutil.move(file, misc_dir)
            except shutil.SameFileError:
                print("Skipping file because it was a duplicate")
    print(fg_good + "Process completed with no errors...\n\n" + fg_reset)
    return dir


def showDir(dir):
    try:
        os.chdir(dir)
    except FileNotFoundError:
        print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
        return

    for file in os.listdir(dir):
        if os.path.isfile(file):
            print(fg_prompt + file + fg_reset)
        else:   # show directories as white
            print(file)

    print(fg_good + "Process completed...\n\n" + fg_reset)
    return dir


def extractDuplicates(dir):  # Still need to find a way to omit multi-disc games
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
                #print("added " + name + " to lst\n")
            else:
                if name not in dupeList:    # only get one instance of each dupe
                    dupeList.append(name)
                #print("added " + name + " to dupe\n")
    #print("namelst: ", nameList)
    ext = "Duplicates"
    new_dir = os.path.join(dir, ext)
    if not os.path.exists(new_dir):
        os.mkdir(ext)
    for file in os.listdir(dir):
        for dupe in dupeList:
            title = os.path.splitext(os.path.basename(file))[0].lower().split(
                "(")[0]   # get lowered title
            if title == dupe.lower():  # split text to remove file ext
                try:
                    print(fg_good + "Moving " + fg_prompt + file +
                          fg_good + " to " + fg_prompt + new_dir + fg_reset)
                    shutil.move(file, new_dir)
                    break   # break here so we don't try moving the same file to the directory again
                # Now this error should never happen, but I'll leave it just incase.
                except shutil.Error:
                    print(fg_error + "Couldn't move " + fg_prompt + file + fg_error + " to " + fg_prompt +
                          new_dir + fg_error + " because another file or directory had the same name.\n" + fg_reset)
    print(fg_good + "Process completed..." + fg_reset + "\n")
    return dir


def extractExtras(dir):

    try:
        os.chdir(dir)
    except FileNotFoundError:
        print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
        return

    ext = "Extras"
    ext_dir = os.path.join(dir, ext)
    if not os.path.exists(ext_dir):
        print(fg_good + "Created directory " + ext_dir + fg_reset)
        os.makedirs(ext)

    extrasList = ["(Beta", "Beta)",
                  "(Proto", "Proto)",
                  "(Demo", "Demo)",
                  "(Tech Demo", "Tech Demo)",
                  "(Debug", "Debug)"
                  "(Kiosk", "Kiosk)"
                  "(Sample", "Sample)"
                  "(Aftermarket", "Aftermarket)"
                  "(Unknown", "Unknown)"
                  "(Unl", "Unl)"
                  "(bootleg", "bootleg)"
                  "[BIOS", "BIOS]"]

    for file in os.listdir(dir):
        if os.path.isfile(file):
            for tag in extrasList:
                if file.__contains__(tag):
                    clean_tag = tag.translate(
                        str.maketrans("", "", string.punctuation))
                    destination = os.path.join(ext_dir, clean_tag)
                    if not os.path.isdir(destination):
                        os.mkdir(destination)
                    print(fg_good + "Moving " + fg_prompt + os.path.basename(file) +
                          fg_good + " to " + fg_prompt + destination + fg_reset)
                    shutil.move(file, destination)
                    break
