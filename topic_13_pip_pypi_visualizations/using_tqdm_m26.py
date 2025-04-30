# let's try importing tqdm
try:
    from tqdm import tqdm # of coruse we could have skipped trying to import it and just use it
except ImportError:
    print("tqdm is not installed. Please install it using 'pip install tqdm'")
    exit(1)

# without tqdm we can not proceed

for _ in tqdm(range(10_000_000)):
    # Simulate some work being done
    pass # we do nothing

# let's count
total = 0
for n in tqdm(range(10_000_000)):
    # Simulate some work being done
    total += n 
print(f"Total: {total}")