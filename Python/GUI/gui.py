import tkinter as tk
from tkinter import messagebox as mb
from tkinter import filedialog
import folder_organizer_tool as fo
import os
import sys
from functools import partial
import text_redirect as tr


TITLE = "Folder Organizer Tool v0.9.0 - Made by Hoswoo"
DARK_BLUE = '#0A3D62'
LIGHT_BLUE = "#7ddeff"
DARK_GREY = "#2C3335"
CONSOLE_BG = '#A1AAB5'
SIZE = "887x575"
FONT_BIG = ('calibre', 12, 'bold')
FONT = ('calibre', 10, 'bold')
FONT_CONSOLE = ('Times', 10, 'normal')

root = tk.Tk()
root.configure(bg=DARK_BLUE)
root.title(TITLE)
root.geometry(SIZE)
root_dir = os.getcwd()

# Dir stuff
dir_frame = tk.Frame(root, bg=DARK_BLUE, height=400, width=300)
dir_var = tk.StringVar()
dir_entry = tk.Entry(dir_frame, textvariable=dir_var, width=41)
dir_sub_frame = tk.Frame(dir_frame, bg=DARK_BLUE)
dir_text = tk.Text(dir_sub_frame, height=25, width=60,
                   bg=CONSOLE_BG, font=FONT_CONSOLE)
dir_scrollbar = tk.Scrollbar(dir_sub_frame, command=dir_text.yview)
dir_text['yscrollcommand'] = dir_scrollbar.set
dir_text.config(state="disabled")
dir_label = tk.Label(dir_frame, text='Choose a directory to work with:',
                     justify="left", font=FONT_BIG, bg=DARK_BLUE, fg=LIGHT_BLUE)


def refresh():
    dir_text.config(state="normal")
    dir_text.delete("1.0", "end")   # Clear entire output
    dir = dir_entry.get()
    try:
        for file in os.listdir(dir):    # List entire directory
            dir_text.insert("end", file + "\n")
        dir_text.see("end")
        dir_text.config(state="disabled")
    except FileNotFoundError:
        print("\nThat directory does not exist!\n")


os.chdir(root_dir)
if not os.path.isfile("last_dir.txt"):
    open("last_dir.txt", "x")
f = open("last_dir.txt", "r")
last_dir = f.read()
f.close()
refresh()


dir_var.set(last_dir)
dir_var.get()


refresh_btn = tk.Button(dir_frame, text="Refresh",
                        command=refresh, bg=DARK_GREY, fg=LIGHT_BLUE)
refresh()


def browseFiles():
    filename = filedialog.askdirectory(initialdir=last_dir,
                                       title="Select a directory")
    # Change label contents
    dir_var.set(filename)
    refresh()


browse_btn = tk.Button(dir_frame,
                       text="Browse",
                       command=browseFiles,
                       bg=DARK_GREY, fg=LIGHT_BLUE)

dev_label = tk.Label(root, text='Made by Hoswoo',
                     font=FONT, bg=DARK_BLUE, fg=LIGHT_BLUE)

# Console stuff
console_frame = tk.Frame(root, bg=DARK_BLUE, height=400, width=300)
console_sub_frame = tk.Frame(console_frame, bg=DARK_BLUE)
console_text = tk.Text(console_sub_frame, height=24,
                       width=60, bg=CONSOLE_BG, font=FONT_CONSOLE)
console_scrollbar = tk.Scrollbar(console_sub_frame, command=console_text.yview)
console_text['yscrollcommand'] = console_scrollbar.set
console_text.config(state="disabled")
console_text.see("end")
# Redirect all console stuff to text box
sys.stdout = tr.TextRedirector(console_text)
sys.stderr = tr.TextRedirector(console_text)


# Functions stuff
functions_frame = tk.Frame(console_frame, bg=DARK_BLUE,  height=200, width=300)
args_var = tk.StringVar()
args_label = tk.Label(functions_frame, text="Argument:",
                      bg=DARK_BLUE, fg=LIGHT_BLUE, font=FONT)
pick_function_label = tk.Label(
    functions_frame, text="Select\nFunction", bg=DARK_BLUE, fg=LIGHT_BLUE, font=FONT)
args_entry = tk.Entry(functions_frame, textvariable=args_var, width=24)


def show_info(opt_var):  # Describe the functions to the user
    opt = opt_var.get()
    if opt == "Extract files containing":
        print(opt + ":\n" + "Extract a substring from a directory.\n")
    if opt == "Keep files containing":
        print(opt + ":\n" + "Keep all files that contain your entered argument. Moves everything else into another directory.\n")
    if opt == "Alphabetize folders":
        print(opt + ":\n" + "Sorts all files in a directory into alphabetical folders.\nSpecify the number of letters per directory for the argument.\n")
    if opt == "Extract all folders in directory":
        print(opt + ":\n" + "Extract all folders in the directory. (This is useful for quickly reverting folder changes).\n")
    if opt == "Extract duplicates":
        print(opt + ":\n" + "This function will find all duplicate ROMs in the directory and move them to a folder for you to manage.\n")
    if opt == "Extract extras":
        print(opt + ":\n" + "Extracts betas, prototypes, demos, unlicensed, aftermarket, BIOS, and other 'extra' ROM's.\n")


def run_function(opt_var):

    opt = opt_var.get()
    curr_dir = dir_var.get()
    os.chdir(root_dir)
    f = open("last_dir.txt", "w")
    f.write(curr_dir)
    f.close()
    args = args_var.get()
    confirmation = mb.askquestion(
        "You are going to " + opt, 'Are you sure you want to do this?', icon='warning')
    if confirmation == 'yes':
        if opt == "Extract files containing":
            if len(opt) < 2:
                print("Your argument is not long enough (2 characters minimum)!")
            else:
                fo.extractSubStr(curr_dir, args)
        if opt == "Extract all folders in directory":
            fo.extractAllFolders(curr_dir)
        if opt == "Keep files containing":
            if len(opt) < 2:
                print("Your argument is not long enough (2 characters minimum)!")
            else:
                fo.keepSubStr(curr_dir, args)
        if opt == "Alphabetize folders":
            try:
                fo.alphabetizeFolders(curr_dir, int(args))
            except TypeError:
                print("\nYou need to specify the number of letters per directory!\n")
            except ValueError:
                args = 3
                print("Could not read an integer, defaulting to " + str(args) + ".")
                fo.alphabetizeFolders(curr_dir, args)
        if opt == "Extract duplicates":
            fo.extractDuplicates(curr_dir)
        if opt == "Extract extras":
            fo.extractExtras(curr_dir)
        refresh()
        console_text.see("end")
    else:
        print("Cancelled the task...\n")


OPTIONS = [
    "Extract files containing",
    "Keep files containing",
    "Alphabetize folders",
    "Extract all folders in directory",
    "Extract duplicates",
    "Extract extras"
]

opt_var = tk.StringVar(root)
opt_var.set(OPTIONS[0])  # Default is 0

functions_menu = tk.OptionMenu(functions_frame, opt_var, *OPTIONS)
info_btn = tk.Button(functions_frame, text="Help", bg=DARK_GREY,
                     fg=LIGHT_BLUE, command=partial(show_info, opt_var), width=10)
run_btn = tk.Button(functions_frame, text="Run", bg=DARK_GREY,
                    fg=LIGHT_BLUE, width=10, command=partial(run_function, opt_var))


def pack_all():
    # dir stuff
    dir_frame.pack(side="left")

    dir_label.grid(row=0, column=0)
    browse_btn.grid(row=1, column=1)
    dir_entry.grid(row=1, column=0, padx=3)
    refresh_btn.grid(row=1, column=2)
    dir_sub_frame.grid(row=2, column=0, columnspan=3)
    dir_text.pack(side="left")
    dir_scrollbar.pack(side="right", fill="y")
    # console stuff
    console_frame.pack(side="right")
    console_sub_frame.grid(row=5, column=0, columnspan=3)
    console_text.pack(side="left")
    console_scrollbar.pack(side="right", fill="y")
    # functions stuff
    functions_frame.grid(row=0, column=0)
    pick_function_label.grid(row=0, column=0)
    functions_menu.grid(row=0, column=1)
    args_label.grid(row=1, column=0)
    args_entry.grid(row=1, column=1)
    run_btn.grid(row=1, column=2)
    info_btn.grid(row=0, column=2)


pack_all()
root.mainloop()
