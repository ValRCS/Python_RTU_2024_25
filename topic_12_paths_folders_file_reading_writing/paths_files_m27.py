# let's talk about files, paths and folders in Python

# first let's tell our starting datetime
# import datetime # standard library
# print("Starting datetime: ", datetime.datetime.now())

# more common is to import just the datetime class from the datetime module
from datetime import datetime
print("Starting datetime: ", datetime.now())

# now let's talk about current working directory
import os # standard library - a bit older than datetime
# os is a module that provides a way of using operating system dependent functionality like reading or writing to the file system
print("Current working directory: ", os.getcwd())

# there is a newer module called pathlib that is more modern and easier to use
# it is part of the standard library since Python 3.4
# this library works beter across multiple operating systems (Windows, Mac, Linux)
# it is also more object oriented and easier to use than os.path    
from pathlib import Path
# Path is a class that represents a filesystem path
# it is a more modern way to work with paths and files in Python
# print current working directory using pathlib
print(f"Current working directory using pathlib: {Path.cwd()}")    

# let's get all files in our current working directory
# i will use glob * to get all files in the current working directory
my_resources = Path.cwd().glob("*") # looks only in current working directory
# glob is a method of the Path class that returns an iterator of all files that match the pattern
# how many?
print("Number of resources in current working directory: ", len(list(my_resources))) # convert to list to get the length

# now let's get all files and get all folders
my_files = []
my_folders = []
for item in Path.cwd().iterdir(): # iterdir is a method of the Path class that returns an iterator of all files and folders in the current working directory
    if item.is_file(): # is_file is a method of the Path class that returns True if the item is a file
        my_files.append(item) # append the file to the list of files
    elif item.is_dir(): # is_dir is a method of the Path class that returns True if the item is a folder
        my_folders.append(item) # append the folder to the list of folders

# print the number of files and folders
print("Number of files in current working directory: ", len(my_files)) # print the number of files
print("Number of folders in current working directory: ", len(my_folders)) # print the number of folders

# let's print first 5 files and folders
print("First 5 files in current working directory: ") # print the first 5 files
for file_stream in my_files[:5]: # print the first 5 files
    print(file_stream) # print the file name

print("First 5 folders in current working directory: ") # print the first 5 folders
for folder in my_folders[:5]: # print the first 5 folders
    print(folder) # print the folder name

# note we see the full path of the file and folder
# this is so called absolute path
# absolute path uniquely identifies a file or folder in the file system

# let's get full absolute path of our current working directory
cwd = Path.cwd() # get current working directory
print("Current working directory: ", cwd) # print the current working directory
parent_folder = cwd.parent # get the parent folder of the current working directory
print("Parent folder of current working directory: ", parent_folder) # print the parent folder of the current working directory

# let's get ALL txt files in parent folder including recursive subfolders

text_files = list(parent_folder.rglob("*.txt")) # rglob is a method of the Path class that returns an iterator of all files that match the pattern recursively in subfolders
# rglob is a method of the Path class that returns an iterator of all files that match the pattern recursively in subfolders
# how many?
print("Number of text files in parent folder: ", len(text_files)) # print the number of text files

# let's print first 3 text files
print("First 3 text files in parent folder: ") # print the first 3 text files
for text_file in text_files[:3]: # print the first 3 text files
    print(text_file) # print the text file name

# how about printing just the file name and also just the file stem and also the file suffix
# file name is the full name of the file including the extension
# file stem is the name of the file without the extension
# file suffix is the extension of the file including the dot
for text_file in text_files[:3]: # print the first 3 text files
    print(f"File name: {text_file.name} File stem: {text_file.stem} File suffix: {text_file.suffix}") # print the file name

# let's find out only files that have rainis in their file name
# if I did not have a file list already I could do this
# rainis_files = list(parent_folder.rglob("*rainis*.txt")) # rglob is a method of the Path class that returns an iterator of all files that match the pattern recursively in subfolders

# instead I will use the existing list of text files and filter them
rainis_files = []
for file_stream in text_files: # loop through the list of text files
    if "rainis" in file_stream.name: # check if rainis is in the file name
        rainis_files.append(file_stream) # append the file to the list of rainis files
    
# how many rainis files?
print("Number of rainis files in parent folder: ", len(rainis_files)) # print the number of rainis files

# let's print all names of rainis files
for rainis_file in rainis_files: # loop through the list of rainis files
    print(rainis_file.name) # print the file name without the path

# now let's see if there is file "rainis.txt" in the list of rainis files
rainis_file = None
for file_stream in rainis_files: # loop through the list of rainis files
    if file_stream.name == "rainis.txt": # check if the file name is rainis.txt
        rainis_file = file_stream # assign the file to the variable rainis_file
        break

print("rainis_file: ", rainis_file) # print the file name with the path

# i could also check existance in current folder of specific file
# let's check if the file rainis.txt exists in the current working directory
# this is a bit more complicated than just checking if the file exists in the list of rainis files
print("rainis.txt exists in current working directory: ", (Path.cwd() / "rainis.txt").exists()) # check if the file exists in the current working directory

# I could have skipped all of the above if I knew that file exists and I am in correct folder

file_name = "rainis.txt" # file name - relative to current working directory

# let's open this file and read it
# we are using so called with context manager
# with open(file_name, "r") as file_stream: # open the file in read mode for English texts
# for other text usually our encoding will be utf-8
# with open(file_name, encoding="utf-8") as file_stream: # open the file in read mode for English texts
# we can use exact string name of file
with open("rainis.txt", encoding="utf-8") as file_stream: # open the file in read mode for English texts
    text = file_stream.read() # read the file content
    # file_stream is now at the end of the file
    # if I want to read the file again I need to seek to the beginning of the file
    # usually there is no need to do this
    # file_stream.seek(0) # seek to the beginning of the file
    # file is still open here
# FILE is CLOSE here automatically by the with statement


print("File content: ", text) # print the file content

# very typical is to readlines

with open("rainis.txt", encoding="utf-8") as file_stream: # open the file in read mode for English texts
    lines = file_stream.readlines() # read the file content line by line
# file is closed here automatically by the with statement
# how many lines?
print("Number of lines in file: ", len(lines)) # print the number of lines
# let's print first 5 lines
for line in lines[:5]: # print the first 5 lines
    print(line.strip()) # print the line without the newline character at the end
    # strip is needed because readlines() returns a list of lines with newline characters at the end
    # if I want to keep the newline character I can use print(line, end="") # print the line with the newline character at the end

# let's only keep the lines that start with "Tu"
tu_lines = [] # create an empty list of lines that start with "Tu"
for line in lines: # loop through the list of lines
    if line.startswith("Tu"): # check if the line starts with "Tu" # create your own logic here
        tu_lines.append(line) # append the line to the list of lines that start with "Tu"
# how many lines that start with "Tu"?
print("Number of lines that start with 'Tu': ", len(tu_lines)) # print the number of lines that start with "Tu"
# I could have done this with list comprehension
# tu_lines = [line for line in lines if line.startswith("Tu")] # list comprehension

# now let's write the lines that start with "Tu" to a new file called "tu_lines.txt"
# I will use the same with statement to open the file in write mode
# I will use utf-8 encoding again
# I will use write mode to write the file
# if file exists it will be overwritten!
# with open("tu_lines.txt", mode = "w", encoding="utf-8") as file_stream: # open the file in write mode for English texts
#     for line in tu_lines: # loop through the list of lines that start with "Tu"
#         file_stream.write(line) # write the line to the file

# i could have written the file in one go using writelines()
with open("tu_lines.txt", mode = "w", encoding="utf-8") as file_stream: # open the file in write mode for English texts
    file_stream.writelines(tu_lines) # write the lines to the file
    # tu_lines SHOULD have \n inside already
    # if not I could have added it here
# file is closed here automatically by the with statement

# if I want to create a new file with timestamp in the name I can do this
# I will use the current datetime to create a unique file name
time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") # get the current datetime and format it to a string
new_file_name = f"tu_lines_{time}.txt" # create a new file name with the current datetime
# let's write the lines that start with "Tu" to a new file called "tu_lines.txt"
with open(new_file_name, mode = "w", encoding="utf-8") as file_stream: 
    # let's add current datetime to the file inside
    file_stream.write(f"File created on: {time}\n") # write the current datetime to the file
    file_stream.writelines(tu_lines) # write the lines to the file


# appending to existing file
# we can ONLY append to existing file if it exists and only at the END of the file
# we can use the same with statement to open the file in append mode
# let's add another file stamp at the end of the file
# we have the new file name already let's append to it
with open(new_file_name, mode = "a", encoding="utf-8") as file_stream: # open the file in append mode for English texts
    # I can use print to append to the file as well
    print("Appending to file: ", new_file_name, file=file_stream) # print the file name
    # print is less used for writing to files because it is slower than write
    file_stream.write(f"File appended on: {time}\n") # write the current datetime to the file
# FILE is closed here automatically by the with statement

# now for the dangerous stuff let's delete some files
# I want to delete all txt files that start with tu_lines in current working directory

# so let's get first
tu_files = list(Path.cwd().glob("tu_lines*.txt")) # get all files that start with tu_lines in current working directory
# how many?
print("Number of tu_lines files in current working directory: ", len(tu_files)) # print the number of tu_lines files

# let's delete them!
# I will use the unlink method of the Path class to delete the file
# unlink is a method of the Path class that deletes the file
for file in tu_files: # loop through the list of tu_lines files
    file.unlink() # delete the file # file has to be Path object
    # unlink is a method of the Path class that deletes the file
    print("Deleted file: ", file) # print the file name

# for very large files we might not want to read all the info at once
# similarly I might not want to write all the info at once
# assuming we have many lines in the file that end with newline character
# we can use the following recipe to read the file line by line and write it to another file

in_file_name = "rainis.txt" # input file name
out_file_name = "rainis_tu_starts.txt" # output file name

with open(in_file_name, encoding="utf-8") as in_file: # open the input file in read mode for English texts
    print(f"Have opened input file: {in_file_name}") # print the input file name
    with open(out_file_name, mode = "w", encoding="utf-8") as out_file:
        print(f"Have opened output file: {out_file_name}")
        # current datetime to the file inside - not required at all
        out_file.write(f"File created on: {datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}\n")
        for line in in_file: # loop through the input file line by line - memory efficient!!
            if line.startswith("Tu"): # use whatever logic you want here
                out_file.write(line) # write the line to the output file
    # here out_file is closed automatically by the with statement
    # in_file is still open here
# here in_file is closed automatically by the with statement            
print(f"Have written lines to output file: {out_file_name}") # print the output file name
print("Both files are closed now") # print the message
# file is closed here automatically by the with statement


