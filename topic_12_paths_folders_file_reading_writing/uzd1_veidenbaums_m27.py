# D:\Github\Python_RTU_2024_25\topic_12_paths_folders_file_reading_writing\veidenbaums.txt

from string import punctuation
from collections import Counter
# Veidenbaums 1a
def file_len_path(fpath, encoding="utf-8"):
    with open(fpath, mode = "r", encoding=encoding) as file_stream:
        # text_lines = file_stream.readlines() # will not work on 1TB file!
        # line_len = len(text_lines)
        # instead we can use simple counter variable
        line_len = 0
        for _ in file_stream: # so we read file one line by line
            # _ means we do not care about the actual line content
            line_len += 1
    return line_len
 
# print(file_len_path("veidenbaums.txt"))
# print my current directory using Path
from pathlib import Path
print(f"Current working directory: {Path.cwd()}")
# so we can use relative path below
# print(file_len_path("topic_12_paths_folders_file_reading_writing/veidenbaums.txt"))
print(file_len_path("topic_12_paths_folders_file_reading_writing/veidenbaums.txt"))

# if we know absolute path, we can use it directly
print(file_len_path("D:/Github/Python_RTU_2024_25/topic_12_paths_folders_file_reading_writing/veidenbaums.txt"))

# alternativelyl if we have backslash in path, we can use raw string using r prefix to ignore escape sequences
print(file_len_path(r"D:\Github\Python_RTU_2024_25\topic_12_paths_folders_file_reading_writing\veidenbaums.txt"))

def get_poem_lines(fpath, encoding="utf-8"):
    with open(fpath, mode = "r", encoding=encoding) as file_stream:
        text = file_stream.readlines()
        poem_lines = []
        for line in text:
            # if not(line.__contains__("*") or line.__contains__("(") or len(line) == 1):
            #     poem_lines.append(line)
            # above could have been written using in syntax instead of __contains__
            line_stripped = line.strip()
            # if "*" in line_stripped or "(" in line_stripped or len(line_stripped) == 0:
            #     continue
            # stronger check for triple asterisks 
            if len(line_stripped) == 0 or line_stripped.endswith("***") or line_stripped.startswith("("):
                continue
            # # the rest we append
            poem_lines.append(line) # line because we want to keep the line breaks
        return(poem_lines)
    
clean_poem_lines = get_poem_lines("topic_12_paths_folders_file_reading_writing/veidenbaums.txt")
print(f"Got {len(clean_poem_lines)} lines of poem")

def save_lines(destpath, lines, encoding="utf-8", add_newline=False, newline="\n"):
    with open(destpath, mode = "w", encoding=encoding) as file_stream:
        if add_newline: # i add newline to each line using list comprehension
            lines = [line + newline for line in lines]
        file_stream.writelines(lines)

# now let's save in current folder
save_lines("topic_12_paths_folders_file_reading_writing/veidenbaums_clean.txt", clean_poem_lines)

print(f"Punctuation marks as provided by Python string module: {punctuation}")
# let's add "…" to list of bad_chars
bad_chars = punctuation + "…"
print(f"Bad characters: {bad_chars}")

def clean_punkts(srcpath,destpath, bad_chars = punctuation, encoding="utf-8"):
    """Function to clean punctuation marks from text file
    srcpath - source file path
    destpath - destination file path
    bad_chars - string of characters to be removed
    encoding - file encoding, default is utf-8
    """
    with open(srcpath, mode = "r", encoding=encoding) as read_stream:
        text = read_stream.readlines() # could have read all of text with read()
        clean_lines = []
        for line in text:
            for char in bad_chars:
                line = line.replace(char,"")
            clean_lines.append(line)
    with open(destpath, mode = "w", encoding=encoding) as write_stream:
        write_stream.writelines(clean_lines)

# let's use it on veidenbaums_clean.txt to get veidenbaums_clean_no_punkts.txt
clean_punkts("topic_12_paths_folders_file_reading_writing/veidenbaums_clean.txt", 
             "topic_12_paths_folders_file_reading_writing/veidenbaums_clean_no_punkts.txt",
             bad_chars = bad_chars)

def get_word_usage(srcpath,destpath):
    with open(srcpath, mode = "r", encoding="utf-8") as read_stream:
        text = read_stream.readlines()
    words = []
    for line in text:
        words.extend(line.lower().split())
    word_counts = Counter(words)
    with open(destpath, mode = "w", encoding="utf-8") as write_stream:
        # write header
        write_stream.write("Word, Count\n")
        # for word, count in word_counts.items():
        # if we want them in order let's use most_common method
        for word, count in word_counts.most_common():
            write_stream.write(f"{word}, {count}\n")
    return word_counts

# let's save statistics in a csv file
get_word_usage("topic_12_paths_folders_file_reading_writing/veidenbaums_clean_no_punkts.txt",
                "topic_12_paths_folders_file_reading_writing/veidenbaums_word_usage.csv")