# Folder Organizer Tool - Made by Hoswoo/Hosua
This tool is useful for managing folders with lots of files. I mainly made it to handle my large emulator ROM collection.

CHANGELOG:

5/24/2021 - First revision released. - v0.4-alpha

5/25/2021 - Added Extract duplicate ROM function. - v0.5-alpha

5/26/2021 - Alphabetize letters now lets you pick how many letters you want to use per folder. - v0.6-alpha

5/26/2021 - Output was displaying the wrong directories, this is now fixed. v0.6 removed because nothing else was changed. - v0.6.1-alpha

5/27/2021 - Moving files around is now MUCH faster than before. - v0.7-alpha

DISCLAIMER: 
There are likely bugs present in this program. It worked for me, but it has only been tested a few times, so please back up your files before using this tool!


Some issues that I am aware of (If you find more, please let me know):
1) There is no way to change the directory while the program is running, simply restart the program to do this.
2) If you modify the folders externally while running the program, it will potentially mess things up.
3) The source code is incompatible with Linux (and I assume also Mac)
4) Certain unicode characters (UTF-16+) are not supported. 


How to use:

When you first open the program, you will be prompted to enter the directory to the folder you want to modify.

![1](https://user-images.githubusercontent.com/22788738/119487284-2eb63780-bd27-11eb-84b0-4b78078a5261.png)

The easiest way to get this path is navigate to the folder via file explorer, then copy the path from here.

![copy](https://user-images.githubusercontent.com/22788738/119487089-f7478b00-bd26-11eb-9a68-d7cb82cfac13.png)

Once you enter a valid folder path, you will be given the following options.

![2](https://user-images.githubusercontent.com/22788738/119545166-81601580-bd60-11eb-91bb-7f960d32ce23.png)

1) Remove all except

This will take text entered by the user. The program will go through the entire folder, and delete anything that does not contain this text.
Let's say I have a huge folder containing ROMs from many regions but only wanted to keep one.
In this case, the US ROMs in this folder are labelled as "(U)", therefore that is what I will type because I want to keep all of the US ROMs in the folder.

![3](https://user-images.githubusercontent.com/22788738/119488615-c5372880-bd28-11eb-8845-44ed17fc8960.png)

It will prompt you again to make sure you want to do this, just type y to confirm.

![4](https://user-images.githubusercontent.com/22788738/119488950-1e06c100-bd29-11eb-9f05-a9a81f71af32.png)

It will now show you something like this, and all of the files you didn't want should be gone.

![5](https://user-images.githubusercontent.com/22788738/119489045-3e368000-bd29-11eb-8865-5b369938390a.png)

2) Remove all files containing

This is essentially the opposite of the previous function.
Let's say I wanted to only remove files containing Japanese ROMs in the same folder.
Similar to last time, I would type in (J) to do this. This time it will remove everything containing (J) that's in the folder.

![6](https://user-images.githubusercontent.com/22788738/119489610-d9c7f080-bd29-11eb-862f-fd7500f27f04.png)

Once again it will show you the files being deleted.

![7](https://user-images.githubusercontent.com/22788738/119489771-0aa82580-bd2a-11eb-8012-5e999e6dbc29.png)

And assuming everything went well, the files you didn't want should be deleted.

3) Alphabetize Folders

Alphabetize folders lets you sort all your files alphabetically.
First, it will ask you how many letters you want per folder. I will use 3 as an example.


![8](https://user-images.githubusercontent.com/22788738/119653276-2298ab80-bdf5-11eb-802c-a5d0cf294c17.png)

Once again, just type y to confirm, if nothing went wrong, you will see something like this when it's finished.

![9](https://user-images.githubusercontent.com/22788738/119677940-22a4a580-be0d-11eb-9d46-0172ee00da61.png)

After the process is complete, your directory should look something like this.
NOTE: If any folders are empty after this process, they will automatically be deleted.

![10](https://user-images.githubusercontent.com/22788738/119654243-3abcfa80-bdf6-11eb-9306-045ab1f2ec5a.png)

4) Unalphabetize Folders

This should be self explanatory, this essentially undoes what Alphabetize Folders does. 
However please note that this also affects other folders in the directory as well.
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
















