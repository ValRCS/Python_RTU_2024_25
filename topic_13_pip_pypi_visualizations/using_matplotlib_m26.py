# we will be using sinus so need math
import math # standard library, no need to install it

# let's try importing matplotlib
try:
    import matplotlib.pyplot as plt
    # typically for large libraries we import only what we need
    # in this case we also shorten the name to plt
    # let's also import version
    from matplotlib import __version__ as mpl_version
    # most libraries have __version__ attribute
    # let's check if we have it
    print(f"matplotlib is installed, version: {mpl_version}")
except ImportError:
    print("matplotlib is not installed. Please install it using 'pip install matplotlib'")
    exit(1)
# without matplotlib we can not proceed

# let's create some plots let's start with some linear functions
N = 10
x = list(range(N)) # x values
# y will be x*5 + 4
y = [x_i * 5 + 4 for x_i in x] # y values
print(f"x: {x}")
print(f"y: {y}")

plt.plot(x, y, color="green") # plot x and y
plt.title("y = 5*x + 4\n y2 = x^2\ny3 = 5*sin(x)") # set title
plt.xlabel("x") # set x label
plt.ylabel("y") # set y label
plt.grid() # add grid

# let's add a few more plots

# how about squares?
y2 = [x_i**2 for x_i in x] # y values
plt.plot(x, y2, color="blue", linestyle="dashed") # plot x and y

# let's add a long arrow to the plot
plt.annotate("I am arrow", xy=(x[0], 0), xytext=(x[0], y[0]+10), arrowprops=dict(arrowstyle="->", color="black")) # add arrow

# let's do a sine wave

y3 = []
for x_i in x:
    y3.append(math.sin(x_i)*5) # y values

plt.plot(x, y3, color="red", linestyle="dotted") # plot x and y
plt.show() # show the plot