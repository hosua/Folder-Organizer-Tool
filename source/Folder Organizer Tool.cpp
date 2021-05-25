// Folder Organizer Tool.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <string>
#include <filesystem>
#include <fstream>
#include <vector>
#include <direct.h>	// For chdir // This does not work on linux.
#include <map>	// Python Dictionary equivalent (except this is ordered)
#include <algorithm>
using std::filesystem::directory_iterator;
using namespace std;
using std::filesystem::path;

path getDir() {	// Ask user to enter a directory
	string dirPath;
	cout << "Enter the full directory path (right click to paste from clipboard)\n";	
	getline(cin, dirPath);	// This will cin the entire line instead ending at a space.
	path pathObj(dirPath);
	if (!filesystem::exists(dirPath)) {
		cout << "That directory doesn't exist!\n";
		cout << "Exiting...\n";
		exit(EXIT_FAILURE);
	}
	return pathObj;
}

vector<path> getDirList(const path path, bool ignoreDir=true) {	// Create a vector of all path objects that are files in the directory.
	vector<filesystem::path> dirList;
	try {	// Exception here incase the user enters an empty directory
		for (const auto & file : directory_iterator(path)) {
			filesystem::path filePath(file);
			if (ignoreDir) {
				if (!is_directory(filePath)) 	// If not a directory, it's a file
					dirList.push_back(filePath);	// Append to vector only if it is a file.
			}
			else {
				dirList.push_back(filePath);	// Append to vector only if it is a file.
			}
		}
	} 
	catch (filesystem::filesystem_error){
		cout << "WARNING: Either there are no files in the directory or the directory was invalid.\n";
	}
	return dirList;
}
// const - makes the variable constant
// & tells c++ to reference the address of "file". This essentially makes the data mutable. 
//	On the contrary, returning without referencing the address will return a copy instead of the original, making it immutable.
// * tells c++ to reference the pointer of "file". You can do arithmetic operations with pointers.
void showPath(vector<filesystem::path> dirList, bool nameOnly = false) {
	if (!nameOnly) {	// Get file directories
		for (const auto & file : dirList) {
			cout << file << "\n";
		}
	}
	else {	// Get only file name
		for (const auto & file : dirList) {
			cout << file.stem().string() << endl;
		}
	}
	if (dirList.size() == 0)
		cout << "Directory is empty!";
}
void removeAllExcept(vector<filesystem::path> dirList) {
	string keepStr;
	cout << "\nThis tool will remove all files in the folder that DON'T contain the entered text. \n";
	cout << "For example, if I enter (U), any file in the folder that doesn't have (U) in the file name will be deleted.\n\n";
	cout << "\nEnter the text you wish to ignore (This is case sensitive!)\n";
	cin >> keepStr;
	string user_opt;
	cout << "WARNING: This is an irreversible process! Are you sure? (y/n)\n";
	cin >> user_opt;
	cout << "\n";
	if (user_opt == "y") {
		for (const auto & file : dirList) {
			string fileDirStr = file.string();
			string fileNameStr = file.stem().string();
			if (fileNameStr.find(keepStr) == string::npos) {	// This is how you check if the string contains the substring.
				// I don't really fully understand the logic here, look at this later.
				remove(file);
				cout << "Removed '" + fileNameStr + "' from \n'" + file.parent_path().string() + "'\n";
			}	
		}	// Ignore the rest
	}
	else {
		cout << "\n\nUser entered 'n' or input was invalid. Cancelling the task.\n";
		exit(EXIT_FAILURE);
	}
	cout << "\n\nAll done!\n\n";
}
void removeAllContaining(vector<filesystem::path> dirList) {
	string keepStr;
	cout << "\nThis tool will remove all files in the folder that DO contain the entered text. \n";
	cout << "For example, if I enter (J), all files with (J) in the file name will be deleted.\n\n";
	cout << "\nEnter the text you wish to delete all of (This is case sensitive!)\n";
	cin >> keepStr;
	string user_opt;
	cout << "WARNING: This is an irreversible process! Are you sure? (y/n)\n";
	std::cin >> user_opt;
	std::cout << "\n";
	if (user_opt == "y") {
		for (const auto & file : dirList) {
			string fileDirStr = file.string();
			string fileNameStr = file.stem().string();
			if (fileNameStr.find(keepStr) != string::npos) {	// if substring not in string
				remove(file);
				cout << "Removed '" + fileNameStr + "' from \n'" + file.parent_path().string() + "'\n";
			}
		}	
	}
	else {
		cout << "User entered 'n' or input was invalid.\n Exiting the program...";;
	}
	cout << "\n\nAll done!\n\n";
}
void alphabetizeFolder(filesystem::path path) {	// Organizes all files in a directory to alphabetical folders.
	string user_opt;
	cout << "Are you sure you wish to do this? (y/n)";
	cin >> user_opt;
	if (user_opt != "y") {
		cout << "User entered 'n' or input was invalid.\n Exiting the program...";
		return;
	}
	auto dirList = getDirList(path);
	const filesystem::path rootDir = path;	
    string alphabetUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";	// Get every letter in alphabet
	string alphabetLower = "abcdefghijklmnopqrstuvwxyz";

	filesystem::create_directory("#");
	cout << "Created folder named '#'.\n";
	for(char c : alphabetUpper){	// Create folders for all letters
		string letter = string (1, c);	// This is how you convert a char to its letter string 
		filesystem::create_directory(letter);
		cout << "Created folder named '" + letter + "'.\n";
	}
	// Then move each file into their corresponding folders
	for (char ch : alphabetUpper) {	
		filesystem::path letterPath = filesystem::path(rootDir.string()) / string(1, ch);	// Get each letter's directory
		for (const auto &file : dirList) {
			char firstLetter = toupper(file.stem().string()[0]);	// Ignore case sensitivity
			if (firstLetter == ch) {	// If first letter of filename matches the letter we're currently iterating
				cout << "Copying " + file.stem().string() + " to " + letterPath.stem().string() + ".\n";
				filesystem::copy(file, letterPath);	// copy the file to that path
				cout << "Removing " + file.stem().string() + " from " + rootDir.string() + ".\n";
				filesystem::remove(file);	// remove the file after copying
			}
		}
	}	// After dealing with the alphabet, move the remaining files to the # folder.
	dirList = getDirList(path);	// Update the list and check for what files 
	filesystem::path hashPath = filesystem::path(rootDir.string()) / "#";
	for (filesystem::path file : dirList) {
		cout << "Copying " + file.stem().string() + " to " + hashPath.stem().string() + ".\n";
		filesystem::copy(file, hashPath);	// copy the file to that path
		cout << "Removing " + file.stem().string() + " from " + rootDir.string() + ".\n";
		filesystem::remove(file);	// remove the file after copying it 
	}
	for (const auto & dir : directory_iterator(path)) {	// Remove any remaining directories that are empty
		if (filesystem::is_empty(dir)) {
			cout << "Removing \\" + dir.path().stem().string() + " from " + rootDir.string() + ".\n";
			filesystem::remove(dir);
		}
	}
	cout << "\n\nAll done!\n\n";
}	
void unalphabetizeFolder(filesystem::path path) {	// Moves all files/directories from the subdirectory in the directory
	string user_opt;
	cout << "Are you sure you wish to do this? (y/n)";
	cin >> user_opt;
	if (user_opt == "y") {
		for (const auto & dir : directory_iterator(path)) {
			try {
				if (filesystem::is_directory(path))
					for (const auto & subDir : directory_iterator(dir)) {	// For each file in the subdirectory
						cout << "Copying " << subDir.path() << " to " << path << "\n";
						filesystem::copy(subDir, path);
						cout << "Removing " << subDir.path() << " from " + path.string() + ".\n";
						filesystem::remove(subDir);
					}

				for (const auto & dir : directory_iterator(path)) {	// Remove any remaining directories that are empty
					if (filesystem::is_empty(dir)) {
						cout << "Removing \\" + dir.path().stem().string() + " from " + path.string() + ".\n";
						filesystem::remove(dir);
					}
				}
			}
			catch (filesystem::filesystem_error) {
			}
		}
	}
	else {
		cout << "User entered 'n' or input was invalid. Cancelling the task.\n";
	}
	cout << "\n\nAll done!\n\n";
}
void extractDuplicateTitles(filesystem::path path) {
	// The char we need to check for is '('
	// This is where the title name should stop.
	map<filesystem::path, string> dirMap;
	filesystem::path pathObj(path);
	vector<string> nameList;
	
	for (const auto & file : directory_iterator(path)) {
		char delim = '(';
		filesystem::path filePath(file);
		string fileName = file.path().stem().string();
		int endPos = fileName.find(delim);
		string nameNoRegion = fileName.substr(0, endPos);	// This will get just the title names
		dirMap.insert({filePath, nameNoRegion});
		//std::cout << nameNoRegion << "\n";
	}
	
	for (auto const& [key, val] : dirMap) {	// This is how to iterate through a map
		nameList.push_back(val);	// Here were getting all the names into a vector
	}
	vector<string> dupeList;
	for (int i = 0; i < nameList.size(); i++) {
		int count = std::count(nameList.begin(), nameList.end(), nameList[i]);
		//std::cout << nameList[i] + " appears " << count << " times.\n";	// For debug
		if (count > 1)
			dupeList.push_back(nameList[i]);
	}
	sort(dupeList.begin(), dupeList.end());	// This is how you remove duplicates in a vector. Source: https://stackoverflow.com/questions/1041620/whats-the-most-efficient-way-to-erase-duplicates-and-sort-a-vector
	dupeList.erase(unique(dupeList.begin(), dupeList.end()), dupeList.end());

	const filesystem::path rootDir = path;

	if (dupeList.size() > 0) {
		cout << "\n";
		for (int i = 0; i < dupeList.size(); i++) 
			cout << dupeList[i] << "\n";
		std::string user_opt;
		cout << "\n\nThis tool will move your duplicate ROMs to a folder named 'Duplicates'\n";
		cout << "Note: This tool will check for the first '(' in the file name to get the titles.\n";
		cout << "Therefore, this assumed that your ROMs are titled properly. If they are not, this will not work.\n";
		cout << "Also, if your title has multiple disks, it will be considered a duplicate. Please keep that in mind.\n\n";

		cout << "\nThe titles listed above were detected as duplicates.\nWould you like to move them to their own folder? (y/n)\n\n";
		cin >> user_opt;
		if (user_opt == "y") {
			filesystem::create_directory("Duplicates");
			filesystem::path dupeDir = filesystem::path(rootDir.string()) / "Duplicates";
			vector<filesystem::path> pathList;
			for (auto const&[key, val] : dirMap) {	// Check through map and get all the duplicates now
				if (std::binary_search(dupeList.begin(), dupeList.end(), val)) {	// This is a way to check if the element exists in the vector
					pathList.push_back(key);	
				}
			}
			for (int i = 0; i < pathList.size(); i++) {	// Now moving the dupes to the Duplicates folder
				cout << "Copying " << pathList[i].stem().string() << " to " << dupeDir.string() << "\n";
				filesystem::copy(pathList[i], dupeDir);
				cout << "Removing " << pathList[i].stem().string() << " from " << rootDir.string() << "\n";
				filesystem::remove(pathList[i]);
			}
		}
		else {
			cout << "\n\nUser entered 'n' or input was invalid.\n\n";
			return;
		}
	}
	else {
		cout << "\n\nDid not find any duplicates in the directory!\n\n";
	}
	cout << "\n\nAll done!\n\n";
}
int main()
{
	cout << "Folder Organizer Tool\n\n";
	cout << "  __  __           _        _             _   _                               \n";
	cout << " |  \\/  | __ _  __| | ___  | |__  _   _  | | | | ___  _____      _____   ___  \n";
	cout << " | |\\/| |/ _` |/ _` |/ _ \\ | '_ \\| | | | | |_| |/ _ \\/ __\\ \\ /\\ / / _ \\ / _ \\ \n";
	cout << " | |  | | (_| | (_| |  __/ | |_) | |_| | |  _  | (_) \\__ \\\\ V  V / (_) | (_) |\n";
	cout << " |_|  |_|\\__,_|\\__,_|\\___| |_.__/ \\__, | |_| |_|\\___/|___/ \\_/\\_/ \\___/ \\___/ \n";
	cout << "                                  |___/                                       \n\n\n";
	cout << "DISCLAIMER: I am NOT responsible if anything goes wrong either due to bugs or user-negligence.\n";
	cout << "Please be careful and back up any files before using this tool!\n\n";
	bool badDir = true;
	filesystem::path dir;

	dir = getDir();	// Get directory path object
	cout << "Directory: " << dir << "\n";

	_chdir(dir.string().c_str());	// .string() to get string from path obj, then .c_str() will return the string as a constant
	auto dirList = getDirList(dir);	


	bool quit = false;
	while (!quit) {
		int user_opt;
		cout << "\n\nWhat would you like to do?\n";
		cout << "1) Remove all except\n";
		cout << "2) Remove all files containing\n";
		cout << "3) Alphabetize folders\n";
		cout << "4) Unalphabetize folders\n";
		cout << "5) Show directory\n";
		cout << "6) Extract Duplicate ROMs\n";
		cout << "7) Exit\n";
		cin >> user_opt;

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
		case 6:	
			extractDuplicateTitles(dir);
			break;
		case 7:
			cout << "\nExiting the program...";
			quit = true;
		}
	}
}

