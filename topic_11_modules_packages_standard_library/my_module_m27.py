# one of module design principles
# is that module does not execute any code when imported
# print("Hi I am a module from my_module_m27.py")

my_list = [1,2,3,4,5]
my_string = "RTU Python"
my_dict = {"a": 1, "b": 2, "c": 3}

def my_function():
    print("This is my function from my_module_m27.py")

def add(a, b):
    return a + b

# we use so called main guard to check if the module is run directly or imported
# if the module is run directly, __name__ will be equal to "__main__"
if __name__ == "__main__":
    # modules typically use it for testing purposes
    print("Hi I am a module from my_module_m27.py")
    print("This is the module testing program")
    print(my_list) # this will print the list from the module
    print(my_string) # this will print the string from the module
    print(my_dict) # this will print the dictionary from the module
    print(add(2, 3)) # this will print the result of the add function
    assert add(2, 3) == 5 # this will check if the add function works correctly
    # assert does not print anything if the condition is true