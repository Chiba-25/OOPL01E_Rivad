# Strings are immutable
name = "Steve"
try:
    name[2] = "y"  # This will raise an error
except TypeError as e:
    print(e)  # Explanation: Strings cannot be modified after their creation

# Lists are mutable
many_numbers = [2, 5, 7, 23, 1]
many_numbers[2] = 5000  # Modifies the third element in the list
print(many_numbers)  # Output: [2, 5, 5000, 23, 1]
