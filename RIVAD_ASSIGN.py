# Part 1 Declaration of variables with different data types
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


#Part 2Mutable vs. Immutable Data Types
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


#Part 3: Working with Data Structures
#3.1 Lists
numbers = [2, 5, 7, 2, 2]
numbers.append(10)  # Adds 10 to the end
numbers.remove(5)   # Removes the first occurrence of 5
numbers.pop(0)      # Removes and returns the first element (index 0)
print(numbers)      # Output: [7, 2, 2, 10]
print("Count of 2:", numbers.count(2))  # Output: Count of 2: 2


#3.2 Tuples
my_tuple = (2, 5, 7, 23, 1)
try:
    my_tuple[2] = 5000  # This will raise an error
except TypeError as e:
    print(e)  # Explanation: Tuples are immutable


#3.3 Dictionaries
student_marks = {"John": 67, "Kate": 86, "Trevor": 92, "Jane": 55, "Anne": 79}
student_marks["Kate"] = 99  # Modifies Kate's value
student_marks["Matt"] = 76  # Adds a new key-value pair

print(student_marks.keys())   # Prints all keys
print(student_marks.values()) # Prints all values
print(student_marks.get("Kate"))  # Output: 99
print(student_marks.get("Marky")) # Output: None (does not raise an error)


#Bonus Challenge
# Counting occurrences of names using a dictionary
names = ["John", "Kate", "John", "Anne", "Kate", "John", "Anne"]
name_counts = {}

for name in names:
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1

for name, count in name_counts.items():
    print(f"{name}: {count}")
