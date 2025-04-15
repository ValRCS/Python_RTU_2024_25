#Uzdevums "Lielais rezultāts"
def add_mult(first_number, second_number, third_number):
    """"This function takes 3 numbers as input and returns the result of the two smallest numbers multiplied by the largest number.
    The function takes three parameters:
    a ->> int
    b ->> int
    c ->> int"""
    numbers = [first_number, second_number,   third_number]
    # biggest_number = max(numbers)
    # numbers.remove(biggest_number) # modifies the list in place, so we don't need to create a new list
    # return sum(numbers) * biggest_number
    numbers.sort() # modifies the list in place, so we don't need to create a new list
    # alternative would be to use sorted() function, but it would create a new list
    # sorted_numbers = sorted(numbers)
    return (numbers[0] + numbers[1]) * numbers[-1]

# Test the function with some examples
print(add_mult(1, 2, 3)) # 9
print(add_mult(5, 10, 2)) # 70
print(add_mult(0, 0, 0)) # 0
print(add_mult(-1, -2, -3)) # 5

# how about unlimited number of arguments?
def add_mult_unlimited(*args):
    """This function takes unlimited number of arguments and returns the result of the two smallest numbers multiplied by the largest number.
    The function takes one parameter:
    args ->> int"""
    numbers = list(args) # converts tuple to list
    numbers.sort() # modifies the list in place, so we don't need to create a new list
    return (numbers[0] + numbers[1]) * numbers[-1]
# note this does not work when we only have 1 or 0 arguments

# Test the function with some examples
print(add_mult_unlimited(1, 2, 3)) # 9
print(add_mult_unlimited(10,20,30,5,2,100)) # 700

# alternative take list as input

def add_mult_list(numbers):
    """This function takes a list of numbers as input and returns the result of the two smallest numbers multiplied by the largest number.
    The function takes one parameter:
    numbers ->> list of int"""
    # careful with numbers.sort() as it modifies the list in place!
    # if we want to keep the original list, we can use sorted() function instead
    # numbers.sort() # modifies the list in place, so we don't need to create a new list
    numbers = sorted(numbers) # creates a new sorted list, so we don't modify the original list
    
    return (numbers[0] + numbers[1]) * numbers[-1]#

some_numbers = [5,6,10,2,3]
print(add_mult_list(some_numbers)) # 50
print(add_mult_list([1,2,3])) # 9

# let's make a function that returns an integer
# it asks a custom prompt to the user and checks if the input is an integer
def get_integer(prompt = "Lūdzu ievadiet veselu skaitli ", 
                error_msg = "Kļūda, netika ievadīts vesels skaitlis.") -> int:
    """This function takes a prompt as input and returns an integer.
    The function takes two parameters:
    prompt ->> str
    error_msg ->> str
    The function keeps asking the user for input until a valid integer is entered."""
    while True:
        try:
            return int(input(prompt))
        # so idea is that return is not perform if int throws an error
        except ValueError:
            print(error_msg)

number_1 = get_integer()
number_2 = get_integer("Ievadiet otro skaitli: ")
number_3 = get_integer("Ievadiet trešo skaitli: ")

print(add_mult(number_1, number_2, number_3)) 

