# let's talk about reading and writing files in Python

# first what is a file?
# a file is a collection of data that is stored on a computer or other storage device.

# historically files have been seen as a collection of bytes, but in Python we can see files as a collection of lines of text.
# this is because Python was designed to be easy to read and write, and text files are easier to read and write than binary files.

# note Python lets us read and write binary files as well, but we will not cover that in this course.
# only text files today

# let's start with paths

# we need to know the path to the file we want to read or write.
# a path is a string(or Path object) that specifies the location of a file or directory in the file system.

# so let's talk absolute and relative paths
# what is the difference between absolute and relative paths?
# an absolute path is a complete path to a file or directory, starting from the root of the file system.
# a relative path is a path to a file or directory, starting from the current working directory.

# so how do we determine the current working directory?
# we will use pathlib module to get the current working directory
# this is a built-in module that provides classes representing filesystem paths with semantics appropriate for different operating systems.
from pathlib import Path # again standard library module
current_dir = Path.cwd() # this will give us the current working directory
print(f"current_dir: {current_dir}") # this will give us the current working directory as absolute path

# let's find all text files in the current directory
all_text_files = list(current_dir.glob("*.txt")) # this will give us all text files in the current directory
# how many text files do we have in the current directory?
print(f"all_text_files: {all_text_files}") # this will give us all text files in the current directory

# let's find all text files in the current directory and subdirectories!
# for that we use recursive glob - rglob
# for Path we will use Path(".") to get the current directory
# then we will apply rglob method to get all text files in the current directory and subdirectories
all_text_files_recursive = list(Path(".").rglob("*.txt")) # this will give us all text files in the current directory and subdirectories
# how many do I have?
print(f"How many text files do I have? {len(all_text_files_recursive)}") # this will give us all text files in the current directory and subdirectories

# now how about finding text files that start with rainis and end with .txt?
# we have two ways to do this
# we can filter our existing results or filter again with rglob
# let's filter our existing results
rainis_text_files = []
for file in all_text_files_recursive:
    if file.name.startswith("rainis") and file.name.endswith(".txt"):
        rainis_text_files.append(file)
print(f"rainis_text_files: {rainis_text_files} total num {len(rainis_text_files)}") # this will give us all text files in the current directory and subdirectories that start with rainis and end with .txt

also_rainis_files = list(Path(".").rglob("rainis*.txt")) # this will give us all text files in the current directory and subdirectories that start with rainis and end with .txt
print(f"also_rainis_files: {also_rainis_files} total num {len(also_rainis_files)}") # this will give us all text files in the current directory and subdirectories that start with rainis and end with .txt

# ok let's find out exact absolue path for rainis.txt
rainis_file_results = list(Path(".").rglob("rainis.txt")) # this will give us all text files in the current directory and subdirectories that start with rainis and end with .txt
print(f"rainis_file_results: {rainis_file_results}") # this will give us all text files in the current directory and subdirectories that start with rainis and end with .txt
if rainis_file_results:
    rainis_file = rainis_file_results[0] # this will give us the first result
    print(f"rainis_file: {rainis_file}") # this will give us the first result
    print(f"rainis_file.absolute(): {rainis_file.absolute()}") # this will give us the absolute path of the first result
    print(f"rainis_file.resolve(): {rainis_file.resolve()}") # this will give us the absolute path of the first result

# let's read the file rainis.txt
# we will use open() function to open the file and read it
# we will also use with context manager to open the file

# we need to add encoding to the open() function to read the file correctly
# most popular encodings are utf-8 by far
# full list of supported encodings can be found here: https://docs.python.org/3/library/codecs.html#standard-encodings
with open(rainis_file, "r", encoding="utf-8") as file_stream: # this will open the file in read mode
    text = file_stream.read() # this will read the entire file into a string
    # we have commands to change seek and read less than the entire file
    # but those are rarely used in practice
    # file is still open
# here file is automatically closed after the with block
print(f"text: {text}") # this will print the entire file into a string

# now how about reading file by relative path?
# it sure would be nice to read just rainis.txt file without specifying the full path
# then our script has to be in that location!
# so use cd command to change directory to the location of the script
# cd topic_12_paths_folders_file_reading_writing
# we could also do this with os.chdir() function

# if the file is in current directory we can just use the file name directly
# let's read the file rainis.txt
# we will use open() function to open the file and read it
# we will use readlines() function to read the file line by line
# we will also use with context manager to open the file
# so again "rainis.txt" is in the current directory so we can use this relative path
with open("rainis.txt", "r", encoding="utf-8") as file_stream: # this will open the file in read mode
    lines = file_stream.readlines() # this will read the entire file into a list of strings, each string is a line in the file
    # note readlines keeps new line characters at the end of each line
    # we have commands to change seek and read less than the entire file
    # but those are rarely used in practice
    # file is still open
# how many lines?
print(f"lines: {lines}") # this will print the entire file into a list of strings, each string is a line in the file
print(f"number of lines: {len(lines)}") # this will print the number of lines in the file

# now let's get rows that start with "Kā"
kaa_rows = []
for line in lines:
    if line.startswith("Kā"): # use any  logic you want to filter the lines
        kaa_rows.append(line)
# alternative with list comprehension
# kaa_rows = [line for line in lines if line.startswith("Kā")] # use any  logic you want to filter the lines

# let's print our results
print(f"kaa_rows: {kaa_rows}") # this will print the lines that start with "Kā"
# how many?
print(f"number of lines that start with 'Kā': {len(kaa_rows)}") # this will print the number of lines that start with "Kā"

# so let's save our results to a new file
new_file_name = "kaa_rows.txt" # this will be the name of the new file

# let's use datetime module to create timestamps when writing

from datetime import datetime # this is a built-in module that provides classes for manipulating dates and times.
# this module is used to create timestamps when writing
# so datetime module has datetime class that has now() method to get the current date and time
now = datetime.now() # this will get the current date and time
# now we can use strftime() method to format the date and time as a string
# let's get milliseconds as well
# full list of strftime format codes can be found here: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S:%f") # this will format the date and time as a string

# to save we use write mode "w"
# if the file already exists it will be overwritten !!!
# if the file does not exist it will be created !!!
with open(new_file_name, mode="w", encoding="utf-8") as file_stream: # this will open the file in write mode
    # we can use writelines() function to write the entire list to the file
    # or we could use write to write one line
    file_stream.write("My new file with lines that start with 'Kā'\n") # this will write the header to the file
    file_stream.write(f"Created on {formatted_now}\n") # this will write the timestamp to the file
    # note usage of \n because write does not add new line character at the end of the line
    file_stream.writelines(kaa_rows) # this will write the entire list to the file
    # we can also use print to write to the file
    # it is slower because of more formatting
    # i just need to have open file stream as argument
    finish_time = datetime.now() # this will get the current date and time 
    formatted_finish_time = finish_time.strftime("%Y-%m-%d %H:%M:%S:%f") # this will format the date and time as a string
    print(f"Beidzu {formatted_finish_time}", file=file_stream) # this will write the timestamp to the file
    # print("Beidzu rakstīt", file=file_stream) # this will write the entire list to the file
    # no need for \n because print adds new line character at the end of the line
# again file is closed here - import for writing
# so how do we add to the file?
# we use append mode "a" - we can only append to end of the file
# if the file already exists it will be appended to !!!
# if the file does not exist it will be created !!!

# let's use datetime module to create timestamps when writing and also file name
timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") # this will format the date and time as a string
# _ is just an arbitrary separator - you could anything that is valid in file name
file_name = f"kaa_rows_{timestamp}.txt" # this will be the name of the new file


# first let's write to it in write mode
with open(file_name, mode="w", encoding="utf-8") as file_stream: # this will open the file in write mode
    # we can use writelines() function to write the entire list to the file
    # or we could use write to write one line
    file_stream.write("My new file with lines that start with 'Kā'\n") # this will write the header to the file
    file_stream.write(f"Created on {formatted_now}\n") # this will write the timestamp to the file
    # note usage of \n because write does not add new line character at the end of the line
    file_stream.writelines(kaa_rows) # this will write the entire list to the file
    # we can also use print to write to the file
    # it is slower because of more formatting
    # i just need to have open file stream as argument
    finish_time = datetime.now() # this will get the current date and time 
    formatted_finish_time = finish_time.strftime("%Y-%m-%d %H:%M:%S:%f") # this will format the date and time as a string
    print(f"Beidzu {formatted_finish_time}", file=file_stream) # this will write the timestamp to the file

# AGAIN FILE IS CLOSED HERE - IMPORTANT FOR WRITING
# let's append a bit more
# so let's append to the file
# we will use append mode "a" to append to the file
with open(file_name, mode="a", encoding="utf-8") as file_stream: # this will open the file in append mode
    # we can use writelines() function to write the entire list to the file
    # or we could use write to write one line
    file_stream.write("*"*40 + "\n") # this will write the header to the file
    finish_time = datetime.now() # this will get the current date and time 
    formatted_finish_time = finish_time.strftime("%Y-%m-%d %H:%M:%S:%f")
    file_stream.write(f"Appended on {finish_time}\n") # this will write the timestamp to the file
    # note usage of \n because write does not add new line character at the end of the line

# now let's see recipe to open one file and write to another at the same time
# this is useful for huuuuge files that do not fit in your computer memory
# could work on say 2TB file

in_file = "rainis.txt" # this will be the name of the input file
# out_file = "kaa_texts.txt" # this will be the name of the output file
# again let's add timestamp to the file name\
# timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") # this will format the date and time as a string
out_file = f"kaa_texts_{timestamp}.txt" # this will be the name of the new file

# let's open the input file in read mode and output file in write mode
with open(in_file, mode="r", encoding="utf-8") as in_file_stream:
    print(f"Reading from {in_file}") # this will print the name of the input file
    with open(out_file, mode="w", encoding="utf-8") as out_file_stream: # this will open the file in write mode
        print(f"Writing to {out_file}") # this will print the name of the output file
        # we will use loop to go through incoming file one line at a time
        for line in in_file_stream: # so this loop opens one line at a time - SAVE MEMORY
            # we can use writelines() function to write the entire list to the file
            if line.strip().startswith("Kā"): # use any normal string logic you want to filter the lines
                out_file_stream.write(line) # this will write the line to the output file
    # here out_file is closed
# here in_file_stream is closed


# finally let's get a list of files that we want to delete
# we want delete all lines that start with kaa_ and contain 2025 somewhere in the name

# we could use regular expressions but let's use normal string logic for now
# let's get a list of files that we want to delete
kaa_candidates = []
for file in Path(".").rglob("*.txt"): # this will give us all text files in the current directory and subdirectories
    if file.name.startswith("kaa_") and "2025" in file.name: # use any normal string logic you want to filter the lines
        kaa_candidates.append(file) # this will add the file to the list of files to delete
# let's print the list of files to delete
print(f"kaa_candidates: {kaa_candidates}") # this will print the list of files to delete
# how many files to delete?
print(f"number of files to delete: {len(kaa_candidates)}") # this will print the number of files to delete

# we simply unlink the file to delete it
for file in kaa_candidates:
    file.unlink() # this will delete the file
# this is a method of the Path object that deletes the file
# this unlink works because file is a Path object from glob or rglob method

# so we learned about absolute and relative paths
# we learned to search for files in the current directory and subdirectories
# we learned to open file for reading with open() function
# we learned to open file for writing with open() function
# we learned to open file for appending with open() function

# finally we learned to delete files with unlink() method of the Path object
