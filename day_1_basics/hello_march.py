# In Python we write comments starting with # - hash
# comments are for humans - computer ignores them
# write WHY you are doing something
# when learning also WHAT you are doing
print("Hello March Pythonists!")

# we can write any text in print
# including any UTF-8 emoji
print("Pasmaidīsim par pavasari! ☀🌸☀")

print("Kas tas pa joku")

# In Python single quotes work just like double quotes
print('Šis nav joks')
# this is useful if we want to include the other type quotes inside
print('Alice said "follow the white rabbit" and then ran into the cave')

# let's talk about math
print(2+2)
# different from
print("2+2")
# for simple output we can combine multiple values
print("2 + 2 =",2+2)
print("Valdis","RTU") # by default , separates by single whitespace

print("5*5=", 5*5) # in Python we use * for multiplication

print(100-6) # 94
# division can be a little weird

print(20/8)
print(10/3) # we expect 3.333333333 but....

# we also have // division
print(20 // 8) # we only get integer part

# we also have reminder / similar to modulo operator %
print(10 % 3) # 1
print(11 % 3) # 2
print(12 % 3) # 0

# useful for odd or even
print(10 % 2)
print(11 % 2)

# we can raise powers with **
print(2**3)# two cubed
print(2**8) # one byte of 8 bits

print(2**16)
# for say RGB we can get 16 millions - 24 bits
print(2**24)
print(2**32)

# so we use 64 bit addressing
print(2**64)

# Python has automatic Big Number support
print(10**100)

print(10**100 + 157)

# // gives you integer part
# if you want to round then use round function :)
print(round(3.9))
print(round(3.1415926, 4))

# we can use parenthesis to change normal order of operations
print((2+5)*(7+3))

# we can do some things with + on strings
# so called string concatenation
print("Valdis " + "likes Python")

# suprisingly Python lets you use * with strings and integers
print("Beer 🍺 " * 5)
# useful sometimes for some formatting
print("*"*40)