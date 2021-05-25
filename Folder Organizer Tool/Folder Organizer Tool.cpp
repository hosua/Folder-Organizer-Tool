// Folder Organizer Tool.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <string>
#include <filesystem>
#include <fstream>
#include <vector>
#include <direct.h>	// For chdir
using std::filesystem::directory_iterator;

std::filesystem::path getDir() {	// Ask user to enter a directory
	std::string dirPath;
	std::cout << "Enter the full directory path (right click to copy & paste)\n";	
	std::getline(std::cin, dirPath);	// This will std::cin the entire line instead ending at a space.
	std::filesystem::path pathObj(dirPath);
	if (!std::filesystem::exists(dirPath)) {
		std::cout << "That directory doesn't exist!\n";
		std::cout << "Exiting...\n";
		exit(EXIT_FAILURE);
	}
	return pathObj;
}

std::vector<std::filesystem::path> getDirList(const std::filesystem::path path, bool ignoreDir=true) {	// Create a vector of all path objects that are files in the directory.
	std::vector<std::filesystem::path> dirList;
	try {	// Exception here incase the user enters an empty directory
		for (const auto & file : directory_iterator(path)) {
			std::filesystem::path filePath(file);
			if (ignoreDir) {
				if (!is_directory(filePath)) 	// If not a directory, it's a file
					dirList.push_back(filePath);	// Append to vector only if it is a file.
			}
			else {
				dirList.push_back(filePath);	// Append to vector only if it is a file.
			}
		}
	} 
	catch (std::filesystem::filesystem_error){
		std::cout << "WARNING: Either there are no files in the directory or the directory was invalid.\n";
	}
	return dirList;
}
// const - makes the variable constant
// & tells c++ to reference the address of "file". This essentially makes the data mutable. 
//	On the contrary, returning without referencing the address will return a copy instead of the original, making it immutable.
// * tells c++ to reference the pointer of "file". You can do arithmetic operations with pointers.
void showPath(std::vector<std::filesystem::path> dirList, bool nameOnly = false) {
	if (!nameOnly) {	// Get file directories
		for (const auto & file : dirList) {
			std::cout << file << "\n";
		}
	}
	else {	// Get only file name
		for (const auto & file : dirList) {
			std::cout << file.stem().string() << std::endl;
		}
	}
	if (dirList.size() == 0)
		std::cout << "Directory is empty!";
}
void removeAllExcept(std::vector<std::filesystem::path> dirList) {
	std::string keepStr;
	std::cout << "\nThis tool will remove all files in the folder that DON'T contain the entered text. \n";
	std::cout << "For example, if I enter (U), any file in the folder that doesn't have (U) in the file name will be deleted.\n\n";
	std::cout << "\nEnter the text you wish to ignore (This is case sensitive!)\n";
	std::cin >> keepStr;
	std::string user_opt;
	std::cout << "WARNING: This is an irreversible process! Are you sure? (y/n)\n";
	std::cin >> user_opt;
	std::cout << "\n";
	if (user_opt == "y") {
		for (const auto & file : dirList) {
			std::string fileDirStr = file.string();
			std::string fileNameStr = file.stem().string();
			if (fileNameStr.find(keepStr) == std::string::npos) {	// This is how you check if the string contains the substring.
				// I don't really fully understand the logic here, look at this later.
				remove(file);
				std::cout << "Removed '" + fileNameStr + "' from \n'" + file.parent_path().string() + "'\n";
			}	
		}	// Ignore the rest
	}
	else {
		std::cout << "User entered 'n' or input was invalid. Cancelling the task.\n";
		exit(EXIT_FAILURE);
	}
	std::cout << "\n\nAll done!\n\n";
}
void removeAllContaining(std::vector<std::filesystem::path> dirList) {
	std::string keepStr;
	std::cout << "\nThis tool will remove all files in the folder that DO contain the entered text. \n";
	std::cout << "For example, if I enter (J), all files with (J) in the file name will be deleted.\n\n";
	std::cout << "\nEnter the text you wish to delete all of (This is case sensitive!)\n";
	std::cin >> keepStr;
	std::string user_opt;
	std::cout << "WARNING: This is an irreversible process! Are you sure? (y/n)\n";
	std::cin >> user_opt;
	std::cout << "\n";
	if (user_opt == "y") {
		for (const auto & file : dirList) {
			std::string fileDirStr = file.string();
			std::string fileNameStr = file.stem().string();
			if (fileNameStr.find(keepStr) != std::string::npos) {	// if substring not in string
				remove(file);
				std::cout << "Removed '" + fileNameStr + "' from \n'" + file.parent_path().string() + "'\n";
			}
		}	
	}
	else {
		std::cout << "User either typed 'n' or an invalid input. Exiting...";
	}
	std::cout << "\n\nAll done!\n\n";
}
void alphabetizeFolder(std::filesystem::path path) {	// Organizes all files in a directory to alphabetical folders.
	std::string user_opt;
	std::cout << "Are you sure you wish to do this? (y/n)";
	std::cin >> user_opt;
	if (user_opt != "y") {
		std::cout << "User entered 'n' or input was invalid.\n Exiting the program...";
		return;
	}
	auto dirList = getDirList(path);
	const std::filesystem::path rootDir = path;	
    std::string alphabetUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";	// Get every letter in alphabet
	std::string alphabetLower = "abcdefghijklmnopqrstuvwxyz";

	std::filesystem::create_directory("#");
	std::cout << "Created folder named '#'.\n";
	for(char c : alphabetUpper){	// Create folders for all letters
		std::string letter = std::string (1, c);	// This is how you convert a char to its letter string 
		std::filesystem::create_directory(letter);
		std::cout << "Created folder named '" + letter + "'.\n";
	}
	// Then move each file into their corresponding folders
	for (char ch : alphabetUpper) {	
		std::filesystem::path letterPath = std::filesystem::path(rootDir.string()) / std::string(1, ch);	// Get each letter's directory
		for (const auto &file : dirList) {
			char firstLetter = toupper(file.stem().string()[0]);	// Ignore case sensitivity
			if (firstLetter == ch) {	// If first letter of filename matches the letter we're currently iterating
				std::cout << "Copying " + file.stem().string() + " to " + letterPath.stem().string() + ".\n";
				std::filesystem::copy(file, letterPath);	// copy the file to that path
				std::cout << "Removing " + file.stem().string() + " from " + rootDir.string() + ".\n";
				std::filesystem::remove(file);	// remove the file after copying
			}
		}
	}	// After dealing with the alphabet, move the remaining files to the # folder.
	dirList = getDirList(path);	// Update the list and check for what files 
	std::filesystem::path hashPath = std::filesystem::path(rootDir.string()) / "#";
	for (std::filesystem::path file : dirList) {
		std::cout << "Copying " + file.stem().string() + " to " + hashPath.stem().string() + ".\n";
		std::filesystem::copy(file, hashPath);	// copy the file to that path
		std::cout << "Removing " + file.stem().string() + " from " + rootDir.string() + ".\n";
		std::filesystem::remove(file);	// remove the file after copying it 
	}
	for (const auto & dir : directory_iterator(path)) {	// Remove any remaining directories that are empty
		if (std::filesystem::is_empty(dir)) {
			std::cout << "Removing \\" + dir.path().stem().string() + " from " + rootDir.string() + ".\n";
			std::filesystem::remove(dir);
		}
	}
	std::cout << "\n\nAll done!\n\n";
	return;
}	
void unalphabetizeFolder(std::filesystem::path path) {	// Moves all files/directories from the subdirectory in the directory
	std::string user_opt;
	std::cout << "Are you sure you wish to do this? (y/n)";
	std::cin >> user_opt;
	if (user_opt == "y") {
		for (const auto & dir : directory_iterator(path)) {
			try {

				if (std::filesystem::is_directory(path))
					for (const auto & subDir : directory_iterator(dir)) {	// For each file in the subdirectory
						std::cout << "Copying " << subDir.path() << " to " << path << "\n";
						std::filesystem::copy(subDir, path);
						std::cout << "Removing " << subDir.path() << " from " + path.string() + ".\n";
						std::filesystem::remove(subDir);
					}

				for (const auto & dir : directory_iterator(path)) {	// Remove any remaining directories that are empty
					if (std::filesystem::is_empty(dir)) {
						std::cout << "Removing \\" + dir.path().stem().string() + " from " + path.string() + ".\n";
						std::filesystem::remove(dir);
					}
				}
			}
			catch (std::filesystem::filesystem_error) {
			}
		}
	}
	else {
		std::cout << "User entered 'n' or input was invalid. Cancelling the task.\n";
	}
}
int main()
{
	std::cout << "Folder Organizer Tool\n\n";
	std::cout << "  __  __           _        _             _   _                               \n";
	std::cout << " |  \\/  | __ _  __| | ___  | |__  _   _  | | | | ___  _____      _____   ___  \n";
	std::cout << " | |\\/| |/ _` |/ _` |/ _ \\ | '_ \\| | | | | |_| |/ _ \\/ __\\ \\ /\\ / / _ \\ / _ \\ \n";
	std::cout << " | |  | | (_| | (_| |  __/ | |_) | |_| | |  _  | (_) \\__ \\\\ V  V / (_) | (_) |\n";
	std::cout << " |_|  |_|\\__,_|\\__,_|\\___| |_.__/ \\__, | |_| |_|\\___/|___/ \\_/\\_/ \\___/ \\___/ \n";
	std::cout << "                                  |___/                                       \n\n\n";
	std::cout << "DISCLAIMER: I am NOT responsible if anything goes wrong either due to bugs or user-negligence.\n";
	std::cout << "Please be careful and back up any files before using this tool!\n\n";
	bool badDir = true;
	std::filesystem::path dir;
	dir = getDir();	// Get directory path object
	std::cout << "Directory: " << dir << "\n";

	_chdir(dir.string().c_str());	// .string() to get string from path obj, then .c_str() will return the string as a constant
	auto dirList = getDirList(dir);	


	bool quit = false;
	while (!quit) {
		int user_opt;
		std::cout << "\n\nWhat would you like to do?\n";
		std::cout << "1) Remove all except\n";
		std::cout << "2) Remove all files containing\n";
		std::cout << "3) Alphabetize folders\n";
		std::cout << "4) Unalphabetize folders\n";
		std::cout << "5) Show directory\n";
		std::cout << "6) Exit\n";
		std::cin >> user_opt;

		switch (user_opt) {
		case 1:
			removeAllExcept(dirList);
			break;
		case 2:
			removeAllContaining(dirList);
			break;
		case 3:
			alphabetizeFolder(dir);
			break;
		case 4:
			unalphabetizeFolder(dir);
			break;
		case 5:
			showPath(dirList);
			break;
		case 6:;	
			std::cout << "Exiting the program...";
			quit = true;
		}
	}
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
