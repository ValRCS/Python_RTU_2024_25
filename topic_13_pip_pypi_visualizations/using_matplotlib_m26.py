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
plt.title("y = 5*x + 4") # set title
plt.xlabel("x") # set x label
plt.ylabel("y") # set y label
plt.grid() # add grid
plt.show() # show the plot