# matplotlib is one of the bigget python libraries for data visualization
# it is used for 2D plotting, 3D plotting, and many other types of visualizations
# it is used in many data science and machine learning projects and other projects

# first let's show what Python version we are using
import sys
print(f"Python version: {sys.version}")
# another way of getting the version info
# this is a tuple with the major, minor, and micro version numbers
print(f"Python version info: {sys.version_info}")
# also it is common to show date and time
from datetime import datetime
print(f"Date and time: {datetime.now()}")

# let's try to import matplotlib and see if it is installed
try:
    # it is typical to import submodules from matplotlib since it is so large
    import matplotlib.pyplot as plt # so I import pyplot as plt
    # this is a common practice to avoid name clashes with other libraries
    # import version info from matplotlib and use alias
    # this is a common practice to avoid name clashes with other libraries
    from matplotlib import __version__ as mpl_version
    print(f"matplotlib version: {mpl_version}")
except ImportError:
    print("matplotlib is not installed. Please install it using pip.")
    print("You can do this by running the following command:")

    print("pip install matplotlib")
    # since we have not installed matplotlib, we will not be able to run the rest of the code
    print("Exiting the program.")
    sys.exit(1)

# here we know we have matplotlib installed, so we can run the rest of the code
# let's create a linear function and plot it

# first let's import math
import math # this is standard library, so it is always available
# let's just get x values from 0 to 10 included
N = 50
x = list(range(N+1))
# i will use list comprehension to create y values
# this is a common practice in Python to create lists from other lists
y = [3*x + 2 for x in x] # this is a linear function y = 3x + 2
# let's print what we have so far
print(f"x: {x}")
print(f"y: {y}")
# now let's plot the data using matplotlib

plt.plot(x, y) # this is a simple line plot
# let's add x and y axis and title
plt.xlabel("x values") # this is the x axis label
plt.ylabel("y values") # this is the y axis label
plt.title("Some simple functions") # this is the title of the plot
# let's add square function to the plot
y2 = [x**2 for x in x] # this is a square function y = x^2
plt.plot(x, y2, color = "red", linestyle = "dashed") 

# let's add a sinus function to the plot
y3 = [math.sin(x)*x for x in x] # this is a sinus function y = sin(x)
plt.plot(x, y3, color = "green", linestyle = "dotted") \

# let's add some arrows
# plt.annotate("sin(x)", xy=(5, 5), xytext=(6, 10), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate("x^2", xy=(20, 400), xytext=(20, 420), arrowprops=dict(facecolor='black', shrink=0.05))
# plt.annotate("3x + 2", xy=(5, 17), xytext=(6, 20), arrowprops=dict(facecolor='black', shrink=0.05))

# let's add a grid to the plot
plt.grid(True) # this will add a grid to the plot
# let's add tickmarks to the plot
plt.xticks(range(0, N+1, 5)) # this will add tickmarks to the x axis
plt.yticks(range(0, 1001, 100)) # this will add tickmarks to the y axis

# let's save the plot to a file
# as a png file
# plt.savefig("linear_and_square.png") # this will save the plot to a file called plot.png
# show is left for last
plt.show() # this will show the plot in a new window


