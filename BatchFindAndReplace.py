import argparse
import os
from os import listdir
from os.path import *

prefix = "BatchFindAndReplace.py > "

parser = argparse.ArgumentParser(description="Batch Find and Replace")
parser.add_argument("dir", help="the directory to search")
parser.add_argument("extension", help="the file extension to search for (default: .txt)", default=".txt")
parser.add_argument("find", help="the text to find")
parser.add_argument("replace", help="the text to replace find with")

args = parser.parse_args()

d = args.dir
# Verify that the dir is a directory
if not isdir(d):
    raise Exception(prefix + "Path specified is not a directory!")
    exit()

extension = args.extension
# Append a period if needed
if not extension[0] == ".":
    extension = "." + extension
    
find = args.find
replace = args.replace

# Make sure the user wants to execute the operation
print("--------------------")
print("BatchFindAndReplace.py")
print("Dir: " + d)
print("Extension: " + extension)
print("Find: " + find)
print("Replace: " + replace)
print("---------------------")
# Printed separately for formatting
print(prefix + "Check your arguments before continuing!")
print("Are you sure you want to run BatchFindAndReplace.py? (Y/N)")
if not input("> ").lower() == "y":
    print(prefix + "Exiting.")
    exit()

# Files in the given folder with the given extension (excludes temp files just in case)
files = [file for file in listdir(d) if isfile(join(d, file)) and (extension in file) and (not "-temp" + extension in file)]

for file in files:
    no_ext = file.replace(extension, "")
    try:
        print(prefix + "Finding \"" + find + "\" and replacing it with \"" + replace + "\" in \"" + file + "\"")

        # Open
        file_path = join(d, file)
        open_file = open(file_path, mode="r")
        
        temp_path = join(d, no_ext + "-temp" + extension)
        temp = open(temp_path, mode="w")


        # Read the file, write to temp file
        text = open_file.readlines()
        i = 0
        for line in text:
            text[i] = line.replace(find, replace)
            temp.write(text[i])
            i += 1

        # Close the files so they're not in use
        open_file.close()
        temp.close()

        # Remove the original file (to be overwritten)
        os.remove(file_path)
        # Overwrite
        os.rename(temp_path, file_path)
    except Exception as e:
        print(prefix + "Could not access \"" + file + "\". Skipping.")
    finally:
        if (not open_file.closed) and (not temp.closed):
            # Close the files
            open_file.close()
            temp.close()
        # Clean up any leftovers
        if exists(temp_path):
            os.remove(temp_path)

print(prefix + "Batch Find and Replace complete in \"" + d + "\"!")
        
        
