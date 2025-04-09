# often we might want to split a string and then join in back together 

sentence = "A quick brown fox jumps over the lazy dog"
# we can split it into a list of smaller strings with the split() method
words = sentence.split() # this is a string method
# split splits by ANY whitespace by default
# we could split by other things like a comma or a space or multiple symbols
print(words) # ['A', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

# let's find out index of fox
fox_index = words.index("fox")
print(fox_index) # 3
# let's replace fox with bear
words[fox_index] = "bear"
print(words) # ['A', 'quick', 'brown', 'bear', 'jumps', 'over', 'the', 'lazy', 'dog']

# now I can join it back together with the join() method
# join is a string method, but it joins a list of strings together
# the string that you call join on is the separator
new_string = " ".join(words) # join the list of words with a space in between
print(new_string) # A quick brown bear jumps over the lazy dog

#i could join with anythign like an emoji
new_sentence = "🐻".join(words) # join the list of words with a bear emoji in between
print(new_sentence) # A🐻quick🐻brown🐻bear🐻jumps🐻over🐻the🐻lazy🐻dog

# note in this simple example I could have used replace() to replace fox with bear in the original string
# but this is a good example of how to split and join strings
