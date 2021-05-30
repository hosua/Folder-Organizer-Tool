# Folder Organizer Tool - Made by Hoswoo/Hosua
This tool is useful for managing folders with lots of files. I mainly made it to handle my large emulator ROM collection.

CHANGELOG:

5/24/2021 - First revision released. - v0.4-alpha

5/25/2021 - Added Extract duplicate ROM function. - v0.5-alpha

5/26/2021 - Alphabetize letters now lets you pick how many letters you want to use per folder. - v0.6-alpha

5/26/2021 - Output was displaying the wrong directories, this is now fixed. v0.6 removed because nothing else was changed. - v0.6.1-alpha

5/27/2021 - Moving files around is now MUCH faster than before. - v0.7-alpha

5/27/2021 - User now has the option to either move or remove files for the first 2 options.  
Unalphabetize folders renamed to extract folders as it is a better description for what it does. - v0.7.1-alpha

5/30/2021 - Fixed show directory to now refresh every time changes are made. Fixed a few text outputs that were not behaving correctly. - v0.7.2-alpha

DISCLAIMER: 
There are likely bugs present in this program. It worked for me, but it has only been tested a few times so please back up your files before using this tool!


ISSUES:
1) There is no way to change the directory while the program is running, simply restart the program to do this.
2) If you modify the folders externally while running the program, it will potentially mess things up.
3) The source code is incompatible with Linux (and I assume also Mac)
4) Certain unicode characters (UTF-16+) are not supported. If you run into a file with a character that can't be read, try to narrow down which file it is and rename it.


How to use:

When you first open the program, you will be prompted to enter the directory to the folder you want to modify.

![1](https://user-images.githubusercontent.com/22788738/119487284-2eb63780-bd27-11eb-84b0-4b78078a5261.png)

The easiest way to get this path is navigate to the folder via file explorer, then copy the path from here.

![copy](https://user-images.githubusercontent.com/22788738/119487089-f7478b00-bd26-11eb-9a68-d7cb82cfac13.png)

Once you enter a valid folder path, you will be given the following options.

![2](https://user-images.githubusercontent.com/22788738/119891677-451ae980-bf07-11eb-9670-3f4b4a12b26d.png)

1) Move/Remove all files except

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

2) Move/Remove all files containing

This is essentially the opposite of the previous function.

Let's say I wanted to only move/remove files containing Japanese ROMs in the same folder.

Similar to last time, I would type in (Japan) to do this. This time it will move/remove everything containing (Japan) that's in the folder.

Enter move or remove like last time, then type y to confirm the process.

![6](https://user-images.githubusercontent.com/22788738/119890202-8ad6b280-bf05-11eb-89d3-e9e14ccefbd2.png)

Once again it will show you the files being moved/deleted.

![7](https://user-images.githubusercontent.com/22788738/119890422-d0937b00-bf05-11eb-870d-3ff6c9986341.png)

And assuming everything went well, the files you didn't want should now be moved/deleted.

![7_5](https://user-images.githubusercontent.com/22788738/119890523-ef920d00-bf05-11eb-935e-1465519741e5.png)

3) Alphabetize Folders

Alphabetize folders lets you sort all your files alphabetically.

First, it will ask you how many letters you want per folder. I will use 3 as an example.

![8](https://user-images.githubusercontent.com/22788738/119653276-2298ab80-bdf5-11eb-802c-a5d0cf294c17.png)

Once again, just type y to confirm, if nothing went wrong, you will see something like this when it's finished.

![9](https://user-images.githubusercontent.com/22788738/119677940-22a4a580-be0d-11eb-9d46-0172ee00da61.png)

After the process is complete, your directory should look something like this.

NOTE: If any folders are empty after this process, they will automatically be deleted.

![10](https://user-images.githubusercontent.com/22788738/119654243-3abcfa80-bdf6-11eb-9306-045ab1f2ec5a.png)

4) Extract all folders in directory

If you wish to undo any of the previous functions, this will do just that.

However please keep in mind that this extracts ALL folders in the current directory. Not just the ones that were created by the program.


Once again, you will be prompted with the same message.

![11](https://user-images.githubusercontent.com/22788738/119490733-2a8c1900-bd2b-11eb-9332-9464c7ee8bfc.png)

It will show something similar again.

![12](https://user-images.githubusercontent.com/22788738/119490872-514a4f80-bd2b-11eb-8bad-5e1e30c968a5.png)

Once it's done, your folders will be unorganized again.

![13](https://user-images.githubusercontent.com/22788738/119491000-750d9580-bd2b-11eb-8b5f-e25753ff23ab.png)

5) Show directory

I mainly put this here to let the user verify that they are actually in the right folder.
It will simply show you the directory.

![14](https://user-images.githubusercontent.com/22788738/119491210-aab27e80-bd2b-11eb-82bc-147c86e2e607.png)

6) Extract Duplicate ROMs 

This function will look through a directory and move duplicate titles to their own directory. 
Note that this will only work if your ROMs are properly titled. It will also detect multiple disk ROMs as duplicates too, so please bear that in mind.

Once again, when you select this option, you will be prompted to type y to confirm.

![15](https://user-images.githubusercontent.com/22788738/119540937-01d04780-bd5c-11eb-8b44-4f118df13dc3.png)

Assuming everything went well, your duplicate ROMs should now be in their folder!

![16](https://user-images.githubusercontent.com/22788738/119541818-d7cb5500-bd5c-11eb-8161-c4215abfadc7.png)
















