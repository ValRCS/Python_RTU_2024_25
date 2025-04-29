# let's test our newly installed tqdm package
# tqdm is a package that allows you to create progress bars
# it is an external package that is not included in the standard library
# it is not required but it might be a good idea first to create a virtual environment
# and then install tqdm in that virtual environment

try:
    from tqdm import tqdm
    print("tqdm is installed")
except ImportError:
    print("tqdm is not installed")
    print("Please install tqdm by running: pip install tqdm")

# Let's create a progress bar
for _ in tqdm(range(10_000_000)):
    pass

counter = 0
for _ in tqdm(range(10_000_000)):
    counter += 1
print("Counter:", counter)