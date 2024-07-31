should_quit = False

while not should_quit:
    # Code to execute as long as should_quit is False
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == "quit":
        should_quit = True
