<<<<<<< HEAD
# we can use input to obtain user input
# input always gives us string!
name = input("What is your name friend?")
print(f"Cool so your name is {name}?")
# how about numbers?
# we might get numbers how to convert
weight = input("How many kg of potatoes do you want to buy?")
print(f"Cool so {name} wants to buy {weight} kg of potatoes")
# we probably want to convert this weight to integer
weight = int(weight) # we CAST our weight to integer type
# this could fail if user does not input integer, but about that another day
# I can cast immediately (again it could fail if not float))
price = float(input("How much do potatoes cost in your store?"))

total = weight * price
print(f"So {name} you would pay {total} Euros for {weight} of potatoes")
total = round(total, 2) # so 2 digits after comma
print(f"So {name} you would pay {total} Euros for {weight} of potatoes")
=======
# we can use input to obtain user input
# input always gives us string!
name = input("What is your name friend?")
print(f"Cool so your name is {name}?")
# how about numbers?
# we might get numbers how to convert
weight = input("How many kg of potatoes do you want to buy?")
print(f"Cool so {name} wants to buy {weight} kg of potatoes")
# we probably want to convert this weight to integer
weight = int(weight) # we CAST our weight to integer type
# this could fail if user does not input integer, but about that another day
# I can cast immediately (again it could fail if not float))
price = float(input("How much do potatoes cost in your store?"))

total = weight * price
print(f"So {name} you would pay {total} Euros for {weight} of potatoes")
total = round(total, 2) # so 2 digits after comma
print(f"So {name} you would pay {total} Euros for {weight} of potatoes")
>>>>>>> abc54bc169a692fc32d0309e765f24615a35570d
