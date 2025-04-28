# let's talk about Python modules
# what is a module?
# a module is a file containing Python code. It can define functions, classes, and variables.
# It can also include runnable code. - GENERALLY AVOID RUNNABLE CODE IN MODULES
#  A module allows you to logically organize your Python code.

# philosophically module should not do anything when imported
# but it is not a hard and fast rule
# print("I am a module!")

my_var = 42
my_list = [1, 2, 3, 4, 5]
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

def my_add(x, y):
    return x + y

class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"
    
# if we want to run some code in a module directly, we can use the __name__ variable
# we use so called name guard
# if __name__ is equal to __main__, it means that the module is being run directly, not imported
if __name__ == "__main__":  # this code will only run if the module is run directly, not when imported
    print("I am being run directly!")
    print("This is my module!")
    # i can run all kind of test now or just some code that i want to run when the module is run directly
    print(my_add(50, 170))  # 220
    # typical would be to put some assertions here
    assert(my_add(50, 170) == 220), "my_add function is not working correctly"
    # we could add asserts after creating some objects from MyClass etc
    # assert does nothing if the condition is true
    # this is a simple test, but in real life we would use a testing framework like unittest or pytest
    print("All tests passed!")
