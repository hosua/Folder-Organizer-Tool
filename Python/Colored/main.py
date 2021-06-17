import folder_organizer_tool_colored as fo
from colorama import Fore, Back, Style
import sys
colored = True
fg_prompt = Fore.LIGHTCYAN_EX
fg_good = Fore.GREEN
fg_error = Fore.RED
fg_reset = Fore.RESET
fg_title = Fore.YELLOW
if not colored:
    fg_prompt = ""
    fg_good = ""
    fg_error = ""
    fg_reset = ""
    fg_title = ""
lastDir = "   "
def main():
    global lastDir
    print("Folder Organizer Tool v0.8.0")
    print(fg_title + 	 "  __  __           _        _             _   _                               \n"
	" |  \\/  | __ _  __| | ___  | |__  _   _  | | | | ___  _____      _____   ___  \n"
	" | |\\/| |/ _` |/ _` |/ _ \\ | '_ \\| | | | | |_| |/ _ \\/ __\\ \\ /\\ / / _ \\ / _ \\ \n"
	" | |  | | (_| | (_| |  __/ | |_) | |_| | |  _  | (_) \\__ \\\\ V  V / (_) | (_) |\n"
	" |_|  |_|\\__,_|\\__,_|\\___| |_.__/ \\__, | |_| |_|\\___/|___/ \\_/\\_/ \\___/ \\___/ \n"
	"                                  |___/                                       " + fg_reset + "\n\n")

    print(fg_error + "DISCLAIMER: I am NOT responsible if anything goes wrong or either due to bugs or user-negligence.\n"
    "Please be careful and back up your files before using this tool!\n" + fg_reset)
    while True:
        try:
            user_opt = int(input(fg_prompt + "What would you like to do?\n" + fg_reset +
                                "1. Extract files containing\n"
                                "2. Keep files containing\n"
                                "3. Alphabetize Folders\n"
                                "4. Extract all folders in directory\n"
                                "5. Show directory\n"
                                "6. Extract duplicate ROMs\n"
                                "7. Extract extras (betas, unlicensed, demos, prototypes, etc)\n"
                                "8. Quit" +"\n"))

            if user_opt == 1:
                lastDir = fo.extractSubStr(lastDir)

            if user_opt == 2:
                lastDir = fo.keepSubStr(lastDir)
            if user_opt == 3:
                lastDir = fo.alphabetizeFolders(lastDir)
            if user_opt == 4:
                lastDir = fo.extractAllFolders(lastDir)
            if user_opt == 5:
                lastDir = fo.showDir(lastDir)
            if user_opt == 6:
                lastDir = fo.extractDuplicates(lastDir)
            if user_opt == 7:
                lastDir = fo.extractExtras(lastDir)
            if user_opt == 8:
                print(fg_error + "Exiting the program...\n" + fg_reset)
                break
            
        except ValueError:
            print(fg_error + "Invalid user input!" + fg_reset)

main()