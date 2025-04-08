# let's say we want to make a friendlier user input handling
# we want to let user quit the main loop by typing 'q' or 'Q' or Quit or quit
# we want to let user enter a number and if the user enters a string we want to ask the user to enter a number again

while True:
    user_input = input("Please enter a number (or (Q)uit to quit): ")
    if user_input.lower() == 'q' or user_input.strip().lower().startswith('quit'):
        print("You enter something that starts with 'quit' or 'q'")
        print("Goodbye!")
        break
    try:
        number = float(user_input)
        print(f"You entered the number: {number}")
    except ValueError:
        print("That's not a valid number. Please try again.")
        continue
    print(f"Number {number} squared is: {number ** 2}")
    print(f"Number cubed is: {number ** 3}")