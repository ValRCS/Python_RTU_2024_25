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
