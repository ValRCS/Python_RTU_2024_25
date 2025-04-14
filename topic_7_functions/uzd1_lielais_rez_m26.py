 
def add_mult(a, b, c, verbose = True):
    """	Function to add two smallest numbers and multiply by the largest number.\n
    a: first number - int\n
    b: second number - int\n
    c: third number - int\n\n
    Output:\n
    result: sum of a and b multiplied by c - int
    """
    # skaitli = sorted([a, b, c])  # sakārto no mazākā uz lielāko
    skaitli = [a, b, c]  # saraksts ar argumentiem
    if verbose:
        print(f"VERBOSE: Original list = {skaitli}")
    skaitli.sort()  # sakārto no mazākā uz lielāko - IN-PLACE
    result = (skaitli[0] + skaitli[1]) * skaitli[2]  # aprēķina rezultātu
    if verbose:
        print(f"VERBOSE: ({skaitli[0]} + {skaitli[1]}) * {skaitli[2]} = {result}")
    return result

# test on some arguments
print(add_mult(2, 3, 4)) # (2+3)*4 = 20
print(add_mult(3, 2, 4)) # (2+3)*4 = 20
print(add_mult(4, 3, 2)) # (2+3)*4 = 20

# let's try some negative values as well
print(add_mult(-2, 3, 4)) # (-2+3)*4 = 4
print(add_mult(-3, 2, 4)) # (-3+2)*4 = -4
print(add_mult(-4, 3, 2)) # (-4+2)*3 = -6

# we could have two approaches to offer unlimited number of arguments
# 1. use *args and then sort them
# 2. use a list as an argument and sort it

# let's try the first one
def add_mult_var(*args, verbose = True):
    """	Function to add two smallest numbers and multiply by the largest number.\n
    args: unlimited number of arguments - int\n\n
    Output:\n
    result: sum of two smallest numbers multiplied by the largest number - int
    """
    skaitli = list(args)  # saraksts ar argumentiem
    if verbose:
        print(f"VERBOSE: Original list = {skaitli}")
    skaitli.sort()  # sakārto no mazākā uz lielāko - IN-PLACE
    result = (skaitli[0] + skaitli[1]) * skaitli[-1]  # aprēķina rezultātu
    if verbose:
        print(f"VERBOSE: ({skaitli[0]} + {skaitli[1]}) * {skaitli[-1]} = {result}")
    return result

# let's test it with 5 arguments
print(add_mult_var(2, 6, 7, 3, 4)) # (2+3)*7 = 35

# just as well we could have offered a list as an argument 
# and then sort it
def add_mult_list_in_place(skaitli, verbose = True):
    """	Function to add two smallest numbers and multiply by the largest number.\n
    skaitli: list of numbers - list of int\n\n
    WARNING: Modifies the original list!\n\n
    This function sorts the list in place, which means that the original list is modified.\n
    Output:\n
    result: sum of two smallest numbers multiplied by the largest number - int
    """

    if verbose:
        print(f"VERBOSE: Original list = {skaitli}")
    # if we did not want to modify we could use copy()
    # skaitli = skaitli.copy()  # make a copy of the list
    skaitli.sort()  # sakārto no mazākā uz lielāko - IN-PLACE
    result = (skaitli[0] + skaitli[1]) * skaitli[-1]  # aprēķina rezultātu
    if verbose:
        print(f"VERBOSE: ({skaitli[0]} + {skaitli[1]}) * {skaitli[-1]} = {result}")
    return result

original_list = [2, 6, 7, 3, 4] # list of numbers
print(f"Original list = {original_list}")
print(add_mult_list_in_place(original_list)) # (2+3)*7 = 35
# now original is mutated
print(f"Original list = {original_list}") # [2, 3, 4, 6, 7]


## Better would be out of place solution that does not modify the original list
def add_mult_list(skaitli, verbose = True):
    """	Function to add two smallest numbers and multiply by the largest number.\n
    skaitli: list of numbers - list of int\n\n
    Output:\n
    result: sum of two smallest numbers multiplied by the largest number - int
    """
    if verbose:
        print(f"VERBOSE: Original list = {skaitli}")
    sorted_list = sorted(skaitli)  # sakārto no mazākā uz lielāko - OUT-OF-PLACE
    result = (sorted_list[0] + sorted_list[1]) * sorted_list[-1]  # aprēķina rezultātu
    if verbose:
        print(f"VERBOSE: ({sorted_list[0]} + {sorted_list[1]}) * {sorted_list[-1]} = {result}")
    return result