# handling errors
# product = 1
# while True:
#     try:
#         user_input = input("Please enter an integer or q to quit")
#         if user_input == "q":
#             print("I see you are done here lets break out!")
#             break # end of this loop
#         number = int(user_input) # int can throw ValueError
#         print(f"Cool you entered an integer{number}, good job!")
#     except ValueError:
#         print("Please enter an integer! Try again")
#         continue # we go to beginning of loop!
#     
#     # we can do something with this integer now
#     product *= number
#     print(f"aha after multiplying by {number} we got {product}")
#     
# print("All done our final result is", product)

# we can handle multiple inputs in one try

while True: # this is where continue will go back to
    print("Please enter integers or floating point numbers only!")
    try:
        # either float conversion can throw ValueError
        a = float(input("Enter number 1"))
        b = float(input("Enter number 2 (non zero!)"))
        # we could check for b being 0 here and then continue
        result = a / b # can Throw Division by Zero
        print(f"Great success! {a} / {b} is roughly {result:.4f}")
        break # for now since we did not handle exit
    except ValueError:
        print(f"Hmm one of the inputs is not converted to float: error")
        continue # back to start
    except ZeroDivisionError:
        print(f"Oops! You divided by zero again!")
        continue # technically we do not need this since we have nothing else to do
    
    # above was illustrative
    # personally I would the division in a different try
        
                