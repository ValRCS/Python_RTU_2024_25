# getting user input
# for that we use input function
# input ALWAYS returns string
first_name = input("What is your first name friend?")
print(f"Cool your first name is {first_name}")
# since we always get string
# we might need to cast our input to other data type
# such as int or float
# how many potatoes do you want to buy
weight = input("How many kg of potatoes do you want to buy?")
# so we will want to CAST it to integer (or float)
weight = int(weight) # this could also lead to error if user gives bad input
# we will learn to handle errors a bit later
# we can cast immediately
price = float(input("How much are potatoes in your store?"))
total = weight * price
print(f"Cool, {weight}kg of potatoes would cost {total} Euros")

# we also might want to round a bit
total_rounded = round(total, 2) # so round 2 digits after comma
print(f"Total rounder {total_rounded}")