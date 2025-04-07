# Again while loops work great when we do not know when we will stop
# for fixed size loops
# we have a more concise alternative for loop

# in Python for loops go THROUGH some collection/sequence/iterable

for n in range(5):
    print(f"n is now {n}")
    
print(f"At end of for loop n is {n}")

# so range(5) goes through numbers 0 to 4 included but not 5 !

# fuller syntax for range is range(start, stop) where start is included
# stop is NOT included

# how about from 1 to 7 included
for n in range(1, 8):
    print(f"Working with n {n}")
    
print("outside n is", n)

# actually range has 3 parameters (start, stop,step)
# start is 0 by default
# step is 1 by default

for i in range(100, 200+1, 10):
    print("i is ", i)
    
print("i is outside and is", i)

# if you think about it
# string is a collection/sequence of smaller stings/characters
name = "Valdis"
for c in name: #i could have chose anything else char, t, i, etc
#     print("letter", c)
    print(f"char {c} -> Unicode {ord(c)}")
    
cat = "Dārsijs 🐈"
for c in cat:
    print(f"char {c} -> Unicode {ord(c)}")
    
# sometimes we just want to do something again and again but do not care about loop variable
for _ in range(3): # _ symbolizes that we do not care about the variable
    print("Brushing my teeth")
    
# i could do this 1_000_000 times or more....
total = 0
big = 1_000_000
for n in range(1, big+1): # 1_000 is same as 1000 or even 1_0_0_0 .....
    total += n # of cours we could have used Gaussian formula
print("total is", total)
print("Gauss did it in school like this", big*(big+1)//2)
# actually in Python we can sum ranges
print("also same is", sum(range(1, big+1)))

# of course I can do things inside the for loop
for n in range(12):
    if n % 2 == 0:
        print("We got EVEN", n)
    else: # that is n % 2 == 1
        print("We got ODD", n)
        
# we can also break or continue from for loop
for n in range(10):
    print("n", n)
    if n == 6:
        print("I am out of here!", n)
        break
    
print("Outside n is ", n)