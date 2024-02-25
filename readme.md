# simple, reusable, extensible
- powershell shell script
- json template/settings file
- cli menu with display of template choices
- settings menu with options

create an item list loaded from a list of templates in a json file in the form of an array under a key. loop over the items in the array using a processing function.
	every item will be either be in the form of a hashmap or an item, and will be either a file, a folder, or contents.
- if its a hashmap, see what the key is
	- if the key is a file, make the file and put the values in the file
	- if the key is a folder, make the folder, cd into it and put the values back through the processing function. cd back out after the recursive call
- if its an item see what it is
	- if its a file, make the file
	- if its a folder, make the folder
