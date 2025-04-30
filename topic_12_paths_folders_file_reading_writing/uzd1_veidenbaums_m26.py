# let's write a function for file length

def file_len_path(fpath, encoding="utf-8"):
    """
    Function to count the number of lines in a file.
    :param fpath: Path to the file.
    :param encoding: Encoding of the file.
    :return: Number of lines in the file.
    """
    # optimal solution
    try:
        with open(fpath, "r", encoding=encoding) as f:
            # first very Python
            # return sum(1 for _ in f) # efficient and lazy way to count lines
            # not efficient
            # lines = f.readlines()
            # return len(lines) # works but will load ALL lines into memory
            # so above will not work if you have a very large file say 100GB
            # instead simple solution is to use a for loop
            # and count lines one by one
            count = 0
            for line in f: # key idea we only read one line at a time
                count += 1
            return count
        

    except FileNotFoundError:
        print(f"File {fpath} not found.")
        return 0
    
# let's test it on veidenbaums.txt
# if I try directly it will not work
# because my current working directory is not the same as the file location

# I could use absolute path or relative path
# since we are using \ in Windows we need to escape it
# or use raw string - my preference
# or use forward slash - works in Windows too
file_path = r"D:\Github\Python_RTU_2024_25\topic_12_paths_folders_file_reading_writing\veidenbaums.txt"
print(f"File length: {file_len_path(file_path)}")
# we could also use relative path - topic_12_paths_folders_file_reading_writing\veidenbaums.txt
# print current working directory
from pathlib import Path
print(f"Current working directory: {Path.cwd()}")
relative_path = r"topic_12_paths_folders_file_reading_writing\veidenbaums.txt"
print(f"File length: {file_len_path(relative_path)}")

# let's create function to get a list of poem lines
# poem lines are defined as lines that have some text in them
# in addition these lines do not end with ***
# also exclude lines that start with (
def get_poem_lines(fpath, encoding="utf-8"):
    """
    Function to get a list of poem lines from a file.
    :param fpath: Path to the file.
    :param encoding: Encoding of the file.
    :return: List of poem lines.
    """
    try:
        with open(fpath, "r", encoding=encoding) as f:
            lines = []
            for line in f:
                # strip line and check if it is not empty
                # also check if it does not end with ***
                # also check if it does not start with (
                line_stripped = line.strip() # remove any leading and trailing whitespace characters
                if line_stripped and not line_stripped.endswith("***") and not line_stripped.startswith("("):
                    lines.append(line) # we want to preserve the line as is including the \n at the end
            return lines
    except FileNotFoundError:
        print(f"File {fpath} not found.")
        return []
    
poem_lines = get_poem_lines(file_path)
print(f"Number of poem lines: {len(poem_lines)}")

# let's create a fu nction to save list to destination file
def save_lines(dst, lines, encoding="utf-8", newline=None):
    """
    Function to save a list of lines to a file.
    :param dst: Path to the destination file.
    :param lines: List of lines to save.
    :param encoding: Encoding of the file.
    """
    try:
        with open(dst, mode="w", encoding=encoding) as f:
            for line in lines:
                if newline:
                    f.write(line + newline)
                else:
                    f.write(line) # write line as is including the \n at the end
    except FileNotFoundError:
        print(f"File {dst} not found.")

# let's save the poem lines to a new file
poem_lines_file = Path("topic_12_paths_folders_file_reading_writing/poem_lines.txt")
save_lines(poem_lines_file, poem_lines)


# now let's create a function that cleans bad_chars given a src and saves to dst
# let's import basic punctuation and some other characters
import string # this loads some variables from string module
print(f"Punctuation: {string.punctuation}")
def clean_bad_chars(src, dst, bad_chars=string.punctuation, encoding="utf-8"):
    """
    Function to clean bad characters from a file.
    :param src: Path to the source file.
    :param dst: Path to the destination file.
    :param bad_chars: List of bad characters to remove.
    :param encoding: Encoding of the file.
    """
    try:
        with open(src, "r", encoding=encoding) as f:
            lines = []
            for line in f:
                for char in bad_chars:
                    line = line.replace(char, "") # replace bad char with empty string
                lines.append(line) # we want to preserve the line as is including the \n at the end
        save_lines(dst, lines, encoding=encoding)
    except FileNotFoundError:
        print(f"File {src} not found.")

# let's save to clean_poem_lines.txt
clean_poem_lines_file = Path("topic_12_paths_folders_file_reading_writing/clean_poem_lines.txt")

# turns out we also have to delete …
bad_chars = string.punctuation + "…"
print(f"Bad characters: {bad_chars}")
clean_bad_chars(poem_lines_file, clean_poem_lines_file, bad_chars=bad_chars)

#TODO do the Counter and get statistsics on the poem
