#Task 1: Implement Conditional Statement
print("1. Implement Conditional Statements")
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
print("_____________________________________________________")

#Task 2: Use Loop to Process Data
print("2. Use Loops to Process Data")
print("\nEven numbers from 1 to 20:")
for i in range (1, 21):
    if i % 2 == 0:
        print(i)

#While loop that stops when user enters 0
while True:
    user_input = int(input("\nEnter a number (0 to stop): "))
    if user_input == 0:
        print("Loop stopped.")
        break
print("_____________________________________________________")

#Task 3: Loop Control Statements
print("3. Loop Control Statements")
print("\nModified loop:")
for i in range (1, 21):
    if i % 5 == 0:
        continue #Skip number divisible by 5
    if i > 15:
        break #Stop loop if number is greater than 15
    print(i)