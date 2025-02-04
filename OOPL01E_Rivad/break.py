#example of using break in while loop
while True:
    user_input = input("Enter a word (type 'quit' to exit): ")
    if user_input == 'quit':
        print("Exiting the loop...")
        break
    print(f"You entered: {user_input}")
