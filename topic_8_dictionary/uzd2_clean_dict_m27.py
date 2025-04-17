# 2. Uzdevums - Vārdnīcu labotājs
def replace_dict_value_in_place(d:dict, bad_val, good_val) -> dict:
    """Replace all occurrences of bad_val with good_val in the dictionary d.
    THIS is IN PLACE version, so the original dictionary will be changed.
    Args:
        d (dict): The dictionary to modify.
        bad_val: The value to replace.
        good_val: The value to replace with.
    Returns the modified dictionary.
    """
    for key, value in d.items():
        if value == bad_val:
            d[key] = good_val
    return d

original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 1}
print("OG dict", original_dict)
changed_dict = replace_dict_value_in_place(original_dict, 1, 100)
print("CH dict", changed_dict)
# the original will also be changed in this version!
print("OG dict", original_dict)

# now let's rewrite the function to return a new dictionary but keep original intact
# one way to do it is simply create a copy of dict and modify it
def replace_dict_value_out_of_place(d:dict, bad_val, good_val) -> dict:
    """Replace all occurrences of bad_val with good_val in the dictionary d.
    THIS is OUT OF PLACE version, so the original dictionary will NOT be changed.
    Args:
        d (dict): The dictionary to modify.
        bad_val: The value to replace.
        good_val: The value to replace with.
    Returns the modified dictionary.
    """
    new_dict = d.copy() # create a copy of the original dictionary
    # note I could have also used the same d such as d = d.copy() because d is local reference
    # but this is more readable and clear
    for key, value in new_dict.items():
        if value == bad_val:
            new_dict[key] = good_val
    return new_dict

# so now let's test the function
really_new_dict = replace_dict_value_out_of_place(original_dict, 100, 200)
print("OG dict", original_dict)
print("NEW dict", really_new_dict)
# the original will NOT be changed in this version!