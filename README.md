# Folder Organizer Tool - Made by Hoswoo/Hosua
This tool is useful for managing folders with lots of files. I mainly made it to handle my large emulator ROM collection. Works on Windows/Linux. It can work on Mac, but you will have to run it via Python. 

# Table of Contents
- [Issues](#issues)
- [Changelog](#changelog)
- [Disclaimer](#disclaimer)
- [Current version (v0.8.0+)](#current-version-v080)
  - [Getting Started](#getting-started)
  - [1. Extract files containing](#1-extract-files-containing)
  - [2. Keep files containing](#2-keep-files-containing)
  - [3. Alphabetize Folders](#3-alphabetize-folders)
  - [4. Extract all folders in directory](#4-extract-all-folders-in-directory)
  - [5. Show directory](#5-show-directory)
  - [6. Extract Duplicate ROMs](#6-extract-duplicate-roms)
  - [7. Extract extras](#7-extract-extras)
- [Legacy versions (v0.7.2 and below)](#legacy-versions-v072-and-below)
  - [Getting Started](#getting-started)
  - [1. Move/Remove all files except](#1-moveremove-all-files-except)
  - [2. Move/Remove all files containing](#2-moveremove-all-files-containing)
  - [3. Alphabetize Folders](#3-alphabetize-folders)
  - [4. Extract all folders in directory](#4-extract-all-folders-in-directory)
  - [5. Show directory](#5-show-directory)
  - [6. Extract Duplicate ROMs](#6-extract-duplicate-roms)
# Issues
I don't know how to make the binary files for Mac users. However, if you have python you can just run it via the script instead.

Duplicate folder also detects multiple-disc ROMs as duplicates, will work on a fix.


# Changelog

5/24/2021 - First revision released. - v0.4-alpha

5/25/2021 - Added Extract duplicate ROM function. - v0.5-alpha

5/26/2021 - Alphabetize letters now lets you pick how many letters you want to use per folder. - v0.6-alpha

5/26/2021 - Output was displaying the wrong directories, this is now fixed. v0.6 removed because nothing else was changed. - v0.6.1-alpha

5/27/2021 - Moving files around is now MUCH faster than before. - v0.7-alpha

5/27/2021 - User now has the option to either move or remove files for the first 2 options.  
Unalphabetize folders renamed to extract folders as it is a better description for what it does. - v0.7.1-alpha

5/30/2021 - Fixed show directory to now refresh every time changes are made. Fixed a few text outputs that were not behaving correctly. - v0.7.2-alpha

6/17/2021 - Program was rewritten in Python. Extract extras (betas, demos, etc) feature added. UTF-32 unicode characters are now supported. You can now change directories without having to reopen the program. Colors were added to text (an uncolored version is provided for Windows users because it does not display properly on the native Windows command prompt). The ability to remove files via the program is no longer available. It's better to let the user manually do this instead. - v0.8.0-beta

6/17/2021 - Duplicate ROM grabber was grabbing more ROMs than it was supposed to. This has been fixed. Extract and Keep file functions now no longer grab folders. Weird case sensitivity issue that was present in 0.8.0 was also fixed. v0.8.1-beta

# Disclaimer 
I am not responsible for anything that goes wrong either due to bugs or user-negligence, so please back up your files if you're using this tool on anything important.

If you used the older versions and are wondering why the new version is a much larger file size, it's because I am no longer using C++ to write this. I switched to Python and the executables that are made using Python are just much bigger in size. 

# Current version (v0.8.0+)

Since quite a few things have changed since the previous version, I rewrote the readme. If you are using and older version and don't want to upgrade, the readme for the legacy versions will still be below.

## Getting Started

### Windows Users

If you are using Windows, the native command prompt will not properly display colors. If you don't care about the colors, a non-colored version of the program is provided. Just run the executable of the uncolored version and you should be good to go.

If you want the colors to display properly, you will have to use another terminal. I personally use the VSCode terminal, but I'm sure there are others that work with colors too.

So, if you really want the colors to work on Windows (ignore this if you're getting the uncolored version) first get and install [VSCode](https://code.visualstudio.com/download)

Once VSCode is running, on the top-left, click File>Open Folder, then open the folder you downloaded the tool at.

Once your folder is opened, click Terminal>New Terminal and then a terminal should open. 

![117](https://i.imgur.com/MBGC7HF.png)

Now to open the executable in the terminal, type this into the terminal

> ./Folder-Organizer-Tool-colored-v0.8.0.exe

and then the program should run!

![118](https://i.imgur.com/nFGDl2F.png)

### Linux Users

After downloading the file, extract it to some directory. Open your terminal and use the following commands

> cd /to/your/path

> ./Folder-Organizer-Tool-colored-v0.8.0-linux

![104](https://i.imgur.com/Vji4paQ.png)


### Mac Users, or those using Python in general

If you are running the program with Python, make sure that you first download python. Then download the colorama package via pip

> pip install colorama

Then change to the directory you installed the files and run the program with these commands (replace \path\to\file\ with the directory you used)

> cd \path\to\file\

Then just run main.py via the python command.

> python main.py



## 1. Extract files containing

This function will ask the user for input, then extract any files in the folder that contain that input within their name.

First, you will be prompted to enter your directory. Just copy any paste whatever directory you want to work with and hit enter.

![105](https://i.imgur.com/qTyOFWV.png)

Then you will be prompted to enter a substring to extract. Lets say I'm located in the US, and want to get rid of the Japan ROMs in a directory. To do this, I would type (J) in this case (note that different ROM sets may use different naming conventions).


Once you enter the substring you're extracting, type y to confirm.

![106](https://i.imgur.com/lpe9SBN.png)

Then the program will show you the files being moved, and all the files you wanted to extract will now be in another folder!

![107](https://i.imgur.com/PKOr4qB.png)

## 2. Keep files containing

This function will ask the user for input, and keep any files in the directory that contain that input within their name.

Once again, you will be prompted to enter the directory. If you're using the same directory as before, you can just leave it blank and hit enter.

Let's say I'm in the US and want to move all ROMs from other regions to another folder. In my case, I will type (U) to do this. 

Note: In some ROM sets, some ROMs will be labelled with (USA, Europe), so in that case, I would type (USA to grab all of the US ROMs. Be wary about this as you may miss some ROMs from your region if you're not careful.

![108](https://i.imgur.com/rtuso9g.png)

Once again, type y to confirm and then you will see this, then all the files you didn't want will be in a folder named "Extracted".

![109](https://i.imgur.com/LUKbgx2.png)

## 3. Alphabetize Folders

This function will ask the user how many letters the user wants for each directory, then it will alphabetically-sort all the files into their respective directories.

Once again, you will be prompted to enter the directory.

Then it will ask you how many letters you want per directory. I will use 3 in this example.

![110](https://i.imgur.com/JXUWh3w.png)

Type y to confirm, then you will see this and your files will be sorted alphabetically!

![111](https://i.imgur.com/ANE0wki.png)

## 4. Extract all folders in directory

If you've been following this guide, you might eventually want to undo something. This function will extract every folder in the directory you enter! Note that this includes directories that were not created by the program, so be careful using this!

Just enter the directory, and type y to confirm.

![112](https://i.imgur.com/zacyAY1.png)

All the folders in your directory should now be extracted!

![113](https://i.imgur.com/VajnxAu.png)

## 5. Show directory

Self explanatory, shows all directories and files in the directory.


## 6. Extract Duplicate ROMs

This function will check all ROM titles in the folder and list the duplicates. This works by checking for the first '(' in the file name, so if your ROMs are improperly titled, this will not work!

Note: This also detects mutiple-disc ROMs as duplicates. Please take care to put these ROMs back where you want them!

Just enter the directory you want to use, and type y to confirm.

![114](https://i.imgur.com/KQEVs1m.png)

Then you should see this, and any duplicate titles will now be in another folder!

![115](https://i.imgur.com/zeoNvOZ.png)

## 7. Extract extras

This will grab any ROMs that are tagged as betas, unlicensed, demos, prototypes, etc and put them into a separate folder. Essentially, the more obscure ROMs that most people do not want will be extracted.

Once again, just enter the directory, and type y to confirm.

![116](https://i.imgur.com/NVtOxSA.png)

Now, all of the extra files will be in their own folder!

# Legacy versions (v0.7.2 and below)

This is for the older versions of the program. If you're still using these I recommend you upgrade to the newer version!

## Getting Started

When you first open the program, you will be prompted to enter the directory to the folder you want to modify.

![1](https://user-images.githubusercontent.com/22788738/119487284-2eb63780-bd27-11eb-84b0-4b78078a5261.png)

The easiest way to get this path is navigate to the folder via file explorer, then copy the path from here.

![copy](https://user-images.githubusercontent.com/22788738/119487089-f7478b00-bd26-11eb-9a68-d7cb82cfac13.png)

Once you enter a valid folder path, you will be given the following options.

![2](https://user-images.githubusercontent.com/22788738/119891677-451ae980-bf07-11eb-9670-3f4b4a12b26d.png)

## 1. Move/Remove all files except

This will take text entered by the user. 

The program will go through the entire folder, and either move or delete anything that does not contain this text.

Let's say I have a folder containing ROMs from many regions but only wanted to keep one.

In this case, the US ROMs in this folder are labelled as "(USA)", therefore that is what I will type because I want to keep all of the US ROMs in the folder.

![3](https://user-images.githubusercontent.com/22788738/119889454-8eb60500-bf04-11eb-9cdd-e4ce1096556d.png)

Next it will ask if you wish to move or remove the files. Just type in move or remove to select an option. 

It will then prompt you again to make sure you want to do this, just type y to confirm.

It will now show you something like this.

![4](https://user-images.githubusercontent.com/22788738/119889665-df2d6280-bf04-11eb-8efb-c626cf476a07.png)

All of the files you didn't want should now be gone or in a folder labelled "Separated Files" depending on what you chose to do.

![5](https://user-images.githubusercontent.com/22788738/119889834-1439b500-bf05-11eb-9f00-4370ed241fba.png)

## 2. Move/Remove all files containing

This is essentially the opposite of the previous function.

Let's say I wanted to only move/remove files containing Japanese ROMs in the same folder.

Similar to last time, I would type in (Japan) to do this. This time it will move/remove everything containing (Japan) that's in the folder.

Enter move or remove like last time, then type y to confirm the process.

![6](https://user-images.githubusercontent.com/22788738/119890202-8ad6b280-bf05-11eb-89d3-e9e14ccefbd2.png)

Once again it will show you the files being moved/deleted.

![7](https://user-images.githubusercontent.com/22788738/119890422-d0937b00-bf05-11eb-870d-3ff6c9986341.png)

And assuming everything went well, the files you didn't want should now be moved/deleted.

![7_5](https://user-images.githubusercontent.com/22788738/119890523-ef920d00-bf05-11eb-935e-1465519741e5.png)

## 3. Alphabetize Folders

Alphabetize folders lets you sort all your files alphabetically.

First, it will ask you how many letters you want per folder. I will use 3 as an example. 

This will sort all the files into folders named 'ABC', 'DEF', and so on.

![8](https://user-images.githubusercontent.com/22788738/119653276-2298ab80-bdf5-11eb-802c-a5d0cf294c17.png)

Once again, just type y to confirm, if nothing went wrong, you will see something like this when it's finished.

![9](https://user-images.githubusercontent.com/22788738/119677940-22a4a580-be0d-11eb-9d46-0172ee00da61.png)

After the process is complete, your directory should look something like this.

NOTE: If any folders are empty after this process, they will automatically be deleted.

![10](https://user-images.githubusercontent.com/22788738/119654243-3abcfa80-bdf6-11eb-9306-045ab1f2ec5a.png)

## 4. Extract all folders in directory

If you wish to undo any of the previous functions, this will do just that.

However please keep in mind that this extracts ALL folders in the current directory. Not just the ones that were created by the program.


Once again, you will be prompted with the same message.

![11](https://user-images.githubusercontent.com/22788738/119490733-2a8c1900-bd2b-11eb-9332-9464c7ee8bfc.png)

It will show something similar again.

![12](https://user-images.githubusercontent.com/22788738/119490872-514a4f80-bd2b-11eb-8bad-5e1e30c968a5.png)

Once it's done, your folders will be unorganized again.

![13](https://user-images.githubusercontent.com/22788738/119491000-750d9580-bd2b-11eb-8b5f-e25753ff23ab.png)

## 5. Show directory

I mainly put this here to let the user verify that they are actually in the right folder.
It will simply show you the directory.

![14](https://user-images.githubusercontent.com/22788738/119491210-aab27e80-bd2b-11eb-82bc-147c86e2e607.png)

## 6. Extract Duplicate ROMs 

This function will look through a directory and move duplicate titles to their own directory. 
Note that this will only work if your ROMs are properly titled. It will also detect multiple disk ROMs as duplicates too, so please bear that in mind.

Once again, when you select this option, you will be prompted to type y to confirm.

![15](https://user-images.githubusercontent.com/22788738/119540937-01d04780-bd5c-11eb-8b44-4f118df13dc3.png)

Assuming everything went well, your duplicate ROMs should now be in their folder!

![16](https://user-images.githubusercontent.com/22788738/119541818-d7cb5500-bd5c-11eb-8161-c4215abfadc7.png)
















