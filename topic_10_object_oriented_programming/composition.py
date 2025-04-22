# there is another approach that is a major alternative to inheritance - composition
# this is where we create a new class that will use other classes as attributes
# this is called composition - we can create a new class that will use other classes as attributes


# let's use car, engine, wheels as an example
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print("Engine started with horsepower:", self.horsepower)
        return self
    
    def stop(self):
        print("Engine stopped")
        return self
    
class Wheel:
    def __init__(self, maker, size = 16):
        self.maker = maker
        self.size = size

    def rotate(self):
        print("Wheel of size", self.size, "is rotating")
        return self
    
class Car:
    def __init__(self, model:str, maker:str, engine:Engine, wheels:list[Wheel]):
        self.model = model
        self.maker = maker
        self.engine = engine
        self.wheels = wheels
        print("Car created with model:", self.model, "and maker:", self.maker)

    def start(self):
        self.engine.start()
        for wheel in self.wheels:
            wheel.rotate()
        # add more things that need to be started
        print("Car started")
        return self
    
    def stop(self):
        self.engine.stop()
        # add more things that need to be stopped
        print("Car stopped")
        return self
    
# let's create an engine first
engine = Engine(200)
# let's create 4 wheels made by Michelin standard 16 inches
# i used list comprehension to create 4 wheels
wheels = [Wheel("Michelin") for _ in range(4)] # _ means I do not care about the value


golf = Car("Golf", "Volkswagen", engine, wheels)
golf.start()

golf.stop()

# let's make another car
# we need a new engine
engine2 = Engine(300)
# we need 4 new wheels
wheels2 = [Wheel("Pirelli") for _ in range(4)] # _ means I do not care about the value

# let's create a new car
audi = Car("A4", "Audi", engine2, wheels2)
audi.start()
audi.stop()