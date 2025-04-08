# Declaration of variables with different data types
a_number = 5
a_float = 5.3
my_name = "Stephen"
many_numbers = [2, 5, 7, 23, 1, 4, 10]
more_numbers = range(10)

# Checking data types
print(type(a_number))  # <class 'int'>
print(type(a_float))   # <class 'float'>
print(type(my_name))   # <class 'str'>
print(type(many_numbers))  # <class 'list'>
print(type(more_numbers))  # <class 'range'>

# Testing iterability with for loops
for item in my_name:
    print(item)  # Prints each letter of the string

for item in many_numbers:
    print(item)  # Prints each element in the list

# The following will raise a TypeError because integers are not iterable
try:
    for item in a_number:
        print(item)
except TypeError as e:
    print(e)  # Explanation: Integers are single-valued and not a collection of elements
