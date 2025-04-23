# Let's talk about inheritance and composition in Python.
# Inheritance is a way to form new classes using classes that have already been defined.
# It allows us to create a new class that is a modified version of an existing class.

# for example, let's say we have a class called Animal:
class Animal:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"Animal name: {self.name}")

    def speak(self):
        return "Some sound"
    
# now I can create a new class called Dog that inherits from Animal:
class Dog(Animal):
    # I can overwrit existing methods in the parent class
    def speak(self):
        return "Woof!"
    def bite(self):
        return "Bite!"
    
generic_animal = Animal("Generic Animal")
dog = Dog("Rika")
print(generic_animal.speak())  # Output: Some sound
generic_animal.print_name()  # Output: Animal name: Generic Animal
print(dog.speak())  # Output: Woof!

# dog also has access to the methods of the Animal class, so I can call print_name on it as well:
dog.print_name()

# now let's create Cat class that also inherits from Animal:
class Cat(Animal):
    def speak(self):
        return "Meow!"
    def scratch(self):
        return "Scratch!"
    
cat = Cat("Winnie")
print(cat.speak())  # Output: Meow!

# note that inherited class also have __init_ method, so I can call it in the child class:
# let's make another class called Bird that inherits from Animal:
class Bird(Animal):
    # so we have an extra attribute called color
    # and we want to initialize it in the __init__ method of the Bird class
    def __init__(self, name, color):
        super().__init__(name)  # call the parent class's __init__ method
        # we could have here just done self.name = name, but we want to call the parent class's __init__ method
        self.color = color

    def print_color(self):
        print(f"Bird color: {self.color}")

    # again Bird has all the other methods of Animal class
    def speak(self):
        return "Tweet!"
    
bird = Bird("Tweety", "Yellow")
print(bird.speak())  # Output: Tweet!
bird.print_name()  # Output: Animal name: Tweety
bird.print_color()  # Output: Bird color: Yellow

# the issues with Inheritance is that it is seldom that a clear hierarchy exists.
# Inheritance is a "is-a" relationship, while composition is a "has-a" relationship.

# Composition means we use objects of other classes as part of our class.

# Let's make a car and our car will have engine and wheels.
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print("Engine started")
    
    def stop(self):
        print("Engine stopped")

class Wheel:
    def __init__(self, size=16, manufacturer="Generic"):
        self.manufacturer = manufacturer
        self.size = size

    def rotate(self):
        print("Wheel is rotating")
    
    def stop(self):
        print("Wheel stopped")

class Car:
    def __init__(self, model, make, engine : Engine, wheels: list[Wheel]):
        print("Creating a car")
        self.model = model
        self.make = make
        # here we are using composition, we are using Engine and Wheel classes as part of our Car class
        self.engine = engine  # composition: Car has an Engine
        self.wheels = wheels  # composition: Car has Wheels
        print(f"Car {self.make} {self.model} created with {len(self.wheels)} wheels and engine with {self.engine.horsepower} horsepower")

    def start(self):
        self.engine.start()
        for wheel in self.wheels:
            wheel.rotate()

    def stop(self):
        self.engine.stop()
        for wheel in self.wheels:
            wheel.stop()

# first let's make an engine and wheels:
engine = Engine(150)
# i use list comprehension to create 4 wheels
# this is a list of 4 Wheel objects, each with size 16 and manufacturer "Goodyear"
wheels = [Wheel(size=19, manufacturer="Goodyear") for _ in range(4)] # _ means we do not care about the value

# now that we have engine and wheels, we can create a car:
golf = Car("Golf", "Volkswagen", engine, wheels)
golf.start()  # Output: Engine started, Wheel is rotating (4 times)
# now I can stop the car:
golf.stop()  # Output: Engine stopped, Wheel stopped (4 times)

# I have now access to say 3rd wheel of the car:
print(golf.wheels[2].manufacturer)  # Output: Goodyear


