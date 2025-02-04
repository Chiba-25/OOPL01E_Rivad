#Example of using pass to create an empty block for even numbers
for number in range(1,6):
    if number % 2 == 0:
        pass #do nothing for even numbers
    else:
        print(number)