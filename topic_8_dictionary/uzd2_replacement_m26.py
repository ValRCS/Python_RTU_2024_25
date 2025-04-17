def replace_dict_value(my_dict, bad_value, good_value):
    """"
    IN PLACE replacement of bad_value with good_value in dictionary dict
    :param dict: dictionary to be modified
    :param bad_value: value to be replaced
    :param good_value: value to replace with
    :return: modified dictionary
    """
    #if I wanted a new dictionary here I could simply copy over
    # dict = dict.copy() # so now I have a new copy of incoming dictionary
    for key in my_dict:
        if my_dict[key] == bad_value:
            my_dict[key] = good_value
    return my_dict # technically there is no absolute need to return anything here
# because we are modifying the dictionary in place, but it is a good practice to return something

my_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 1,
    'e': 2,	
}

print(f"OG dict: {my_dict}")
# let's replace 2 with 7
dict_result = replace_dict_value(my_dict, 2, 7)

print(f"New dict: {dict_result}")
# let's look at OG again
print(f"OG dict: {my_dict}")

# now let's see how we could do OUT OF PLACE replacement
# with dict comprehension

def replace_dict_value_out_of_place(my_dict, bad_value, good_value):
    """
    OUT OF PLACE replacement of bad_value with good_value in dictionary dict
    :param dict: dictionary to be modified
    :param bad_value: value to be replaced
    :param good_value: value to replace with
    :return: modified dictionary
    """
    # return {key: (good_value if value == bad_value else value) for key, value in dict.items()}
    # let's do it with loop
    new_dict = {}
    for key, value in my_dict.items():
        if value == bad_value:
            new_dict[key] = good_value
        else:
            new_dict[key] = value

    return new_dict
