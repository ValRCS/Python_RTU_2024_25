# handling errors

product = 1

while True:
    try:
        user_input = input("Please enter an integer or q to quit")
        if user_input == "q":
            print("I see you are done here lets break out!")
            break # end of this loop
        number = int(user_input) # int can throw ValueError
        print(f"Cool you entered an integer{number}, good job!")
    except ValueError:
        print("Please enter an integer! Try again")
        continue # we go to beginning of loop!
    
    # we can do something with this integer now
    product *= number
    print(f"aha after multiplying by {number} we got {product}")
    
print("All done our final result is", product)