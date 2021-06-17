from colorama import Fore, Back, Style
import os
import shutil
import string
colored = True
fg_prompt = Fore.LIGHTCYAN_EX
fg_good = Fore.GREEN
fg_error = Fore.RED
fg_reset = Fore.RESET
if not colored:
    fg_prompt = ""
    fg_good = ""
    fg_error = ""
    fg_reset = ""

def extractSubStr(prevDir):
    dir = input(fg_prompt + "Enter the directory you wish to work with (Leave blank to use previous directory):" + fg_reset + "\n")
    if not dir == "":
        try:
            os.chdir(dir)
        except FileNotFoundError:
            print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
            return ""
    else:
        print(fg_good + "Using the previous directory " + fg_prompt + prevDir + fg_reset)
        dir = prevDir
        try:
            os.chdir(dir)
        except FileNotFoundError and OSError:
            print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
            return ""
    subStr = input(fg_prompt + "Enter the substring you wish to extract:" + fg_reset + "\n").lower()
    confirm = input(fg_prompt + "Are you sure you wish to do this? (y/n) " + fg_reset + "\n").lower()
    if confirm == "y":
        new_dir = os.path.join(dir, subStr)
        if not os.path.exists(new_dir):
            print(fg_good + "Created directory " + new_dir + fg_reset)
            os.makedirs(subStr)
        for item in os.listdir(dir):
            if os.path.isfile(item):    # make sure were working with a file
                if item.lower().__contains__(subStr.lower()):
                    shutil.move(item, new_dir)
                    print(fg_good + "Moving " + fg_prompt + item + fg_good + " to " + fg_prompt + new_dir + fg_reset)
        print(fg_good + "Process completed with no errors...\n\n" + fg_reset)
        return dir
    else:
        print(fg_error + "User did not confirm, stopping process..." + fg_reset + "\n")
        return ""

def keepSubStr(prevDir):
    dir = input(fg_prompt + "Enter the directory you wish to work with (Leave blank to use previous directory):" + fg_reset + "\n")
    if not dir == "":
        try:
            os.chdir(dir)
        except FileNotFoundError:
            print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
            return ""
    else:
        print(fg_good + "Using the previous directory " + fg_prompt + prevDir + fg_reset)
        dir = prevDir
        try:
            os.chdir(dir)
        except FileNotFoundError and OSError:
            print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
            return ""
    
    subStr = input(fg_prompt + "Enter the substring you wish to keep:" + fg_reset + "\n").lower()

    confirm = input(fg_prompt + "Are you sure you wish to do this? (y/n) " + fg_reset + "\n").lower()
    if confirm == "y":
        extr = "Extracted"
        new_dir = os.path.join(dir, extr)
        if not os.path.exists(new_dir):
            print(fg_good + "Created directory " + new_dir + fg_reset)
            os.makedirs(extr)
        for item in os.listdir(dir):
            if os.path.isfile(item):    # make sure were working with a file
                print("item", item.lower(), "substr", subStr)
                if not subStr in item.lower():   
                    print(fg_good + "Moving " + fg_prompt + item + fg_good + " to " + fg_prompt + new_dir + fg_reset)
                    shutil.move(item, new_dir)
        print(fg_good + "Process completed with no errors...\n\n" + fg_reset)
        return dir
    else:
        print(fg_error + "User did not confirm, stopping process..." + fg_reset + "\n")
        return ""

def extractAllFolders(prevDir):
    dir = input(fg_prompt + "Enter the directory you wish to work with (Leave blank to use previous directory):" + fg_reset + "\n")
    if not dir == "":
        try:
            os.chdir(dir)
        except FileNotFoundError:
            print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
            return ""
    else:
        print(fg_good + "Using the previous directory " + fg_prompt + prevDir + fg_reset)
        dir = prevDir
        try:
            os.chdir(dir)
        except FileNotFoundError and OSError:
            print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
            return ""
    confirm = input(fg_prompt + "Are you sure you wish to do this? (y/n) " + fg_reset + "\n").lower()
    if confirm == "y":
        for item in os.listdir(dir):
            new_path = os.path.join(dir, item)
            if os.path.isdir(new_path): # if new_item is a dir
                for file in os.listdir(new_path):
                    filePath = os.path.join(new_path, file)
                    shutil.move(filePath, dir) # move file to root dir
                    print(fg_good + "Moving " + fg_prompt + file + fg_good + " to " + fg_prompt + dir + fg_reset) 

        for item in os.listdir(dir):
            new_path = os.path.join(dir, item)
            if os.path.isdir(new_path) and len(os.listdir(new_path)) == 0:
                print(fg_error + "Removing " + new_path + fg_reset)
                os.rmdir(new_path)
        print(fg_good + "Process completed with no errors...\n\n" + fg_reset)
        return dir
    else:
        print(fg_error + "User did not confirm, stopping process..." + fg_reset + "\n")
        return ""

def alphabetizeFolders(prevDir):

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
        lastFolder = "" # Handle any leftover letters
        if currAlpha != string.ascii_uppercase:
            for letter in string.ascii_uppercase:
                if letter not in currAlpha:
                    lastFolder += letter
                    print(lastFolder)
        if lastFolder != "":
            folderNames.append(lastFolder)
        return folderNames
    
    dir = input(fg_prompt + "Enter the directory you wish to work with (Leave blank to use previous directory):" + fg_reset + "\n")
    if not dir == "":
        try:
            os.chdir(dir)
        except FileNotFoundError:
            print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
            return ""
    else:
        print(fg_good + "Using the previous directory " + fg_prompt + prevDir + fg_reset)
        dir = prevDir
        try:
            os.chdir(dir)
        except FileNotFoundError and OSError:
            print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
            return ""
    
    numLetters = int(input(fg_prompt + "How many letters per directory?" + fg_reset + "\n"))
    confirm = input(fg_prompt + "Are you sure you wish to do this? (y/n) " + fg_reset + "\n").lower()
    if confirm == "y":
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
                    if file[0].upper() in os.path.basename(folder): 
                        print(fg_good + "Moving " + fg_prompt + file + fg_good + " to " + fg_prompt + folder + fg_reset)
                        shutil.move(file, new_dir)   
        
        for file in os.listdir(dir):    # move the left over filse that didn't get sorted into #
            if os.path.isfile(file):
                print(fg_good + "Moving " + fg_prompt + file + fg_good + " to " + fg_prompt + misc_dir + fg_reset)
                shutil.move(file, misc_dir)
        
        print(fg_good + "Process completed with no errors...\n\n" + fg_reset)
        return dir
    else:
        print(fg_error + "User did not confirm, stopping process..." + fg_reset + "\n")
        return ""
def showDir(prevDir):
    dir = input(fg_prompt + "Enter the directory you wish to work with (Leave blank to use previous directory):" + fg_reset + "\n")
    if not dir == "":
        try:
            os.chdir(dir)
        except FileNotFoundError:
            print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
            return ""
    else:
        print(fg_good + "Using the previous directory " + fg_prompt + prevDir + fg_reset)
        dir = prevDir
        try:
            os.chdir(dir)
        except FileNotFoundError and OSError:
            print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
            return ""

    for file in os.listdir(dir):
        if os.path.isfile(file):
            print(fg_prompt + file + fg_reset)
        else:   # show directories as white
            print(file)

    print(fg_good + "Process completed...\n\n" + fg_reset)
    return dir

def extractDuplicates(prevDir):
    dir = input(fg_prompt + "Enter the directory you wish to work with (Leave blank to use previous directory):" + fg_reset + "\n")
    if not dir == "":
        try:
            os.chdir(dir)
        except FileNotFoundError:
            print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
            return ""
    else:
        print(fg_good + "Using the previous directory " + fg_prompt + prevDir + fg_reset)
        dir = prevDir
        try:
            os.chdir(dir)
        except FileNotFoundError and OSError:
            print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
            return ""
    confirm = input(fg_prompt + "Are you sure you wish to do this? (y/n) " + fg_reset + "\n").lower()
    if confirm == "y":
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
                title = os.path.splitext(os.path.basename(file))[0].lower().split("(")[0]   # get lowered title
                if title == dupe.lower():  # split text to remove file ext
                    try:
                        print(fg_good + "Moving " + fg_prompt + file + fg_good  + " to " + fg_prompt + new_dir + fg_reset)
                        shutil.move(file, new_dir)
                        break   # break here so we don't try moving the same file to the directory again
                    except shutil.Error:    # Now this error should never happen, but I'll leave it just incase.
                        print(fg_error + "Tried moving " + fg_prompt + file + fg_error  + " to " + fg_prompt + new_dir + fg_error + " but that file was already there. Ignoring...\n" + fg_reset)
        print(fg_good + "Process completed with no errors..." + fg_reset + "\n")
        return dir
    else: 
        print(fg_error + "User did not confirm, stopping process..." + fg_reset + "\n")
        return ""
def extractExtras(prevDir):
    dir = input(fg_prompt + "Enter the directory you wish to work with (Leave blank to use previous directory):" + fg_reset + "\n")
    if not dir == "":
        try:
            os.chdir(dir)
        except FileNotFoundError:
            print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
            return ""
    else:
        print(fg_good + "Using the previous directory " + fg_prompt + prevDir + fg_reset)
        dir = prevDir
        try:
            os.chdir(dir)
        except FileNotFoundError and OSError:
            print(fg_error + "Bad directory... stopping process." + fg_reset + "\n")
            return ""
    confirm = input(fg_prompt + "Are you sure you wish to do this? (y/n) " + fg_reset + "\n").lower()
    if confirm == "y":
        ext = "Extras"
        ext_dir = os.path.join(dir, ext)
        if not os.path.exists(ext_dir):
            print(fg_good + "Created directory " + ext_dir + fg_reset)
            os.makedirs(ext)

        extrasList = ["(Beta", "Beta)", "(Proto", "Proto)", "(Demo", "Demo)", "(Aftermarket", "(Tech Demo", "(Unknown", "(Sample", "(Unl", "[BIOS]"]

        for file in os.listdir(dir):
            if os.path.isfile(file):
                for tag in extrasList:
                    if file.__contains__(tag):
                        print(fg_good + "Moving " + fg_prompt + file + fg_good + " to " + fg_prompt + ext_dir + fg_reset) 
                        shutil.move(file, ext)
                        break
                    
        print(fg_good + "Process completed with no errors...\n\n" + fg_reset)
        return dir
    else:
        print(fg_error + "User did not confirm, stopping process..." + fg_reset + "\n")
        return ""