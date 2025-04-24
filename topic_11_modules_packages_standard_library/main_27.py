# this is my main program that will use modules from other files
import my_module_m27 # this will import the module and execute it
# we gain namespace my_module_m27 we can use to access the module
# we can use the module by prefixing it with the module name

# so modules offer us the following benefits:
# 1. code reusability - we can use the same module in different programs
# 2. code organization - we can organize our code into different modules
# 3. code testing - we can test our modules separately from the main program
# 4. code encapsulation - we can hide the implementation details of the module from the main program
# 5. code readability - we can make our code more readable by using modules
# 6. code maintainability - we can make our code more maintainable by using modules

# so where does Python look for modules?
# let's find out by importing the sys module and printing the sys.path variable
import sys # sys is standard library module that provides access to system-specific parameters and functions# 
# full list of standard library modules can be found here: https://docs.python.org/3/library/index.html


def main(): # In Python main() is not required, but it is a good practice to use 
    print("This is the main program")
    print("It will use modules from other files")
    print(f"Our module search path is: {sys.path}")
    # we can see that the first entry is the current directory
    # this means we have to be a bit careful with naming our own modules
    # we should not reuse names of standard library modules
    # otherwise we might get unexpected results


    print(my_module_m27.my_list) # this will print the list from the module
    print(my_module_m27.my_string) # this will print the string from the module
    print(my_module_m27.my_dict) # this will print the dictionary from the module
    print(my_module_m27.add(2, 3)) # this will print the result of the add funct

# typically we would start the program here
# first we will check if program is started directly or imported
if __name__ == "__main__":
    # we could add say config() here
    main()
    # also maybe a function called cleanup() to clean up the program