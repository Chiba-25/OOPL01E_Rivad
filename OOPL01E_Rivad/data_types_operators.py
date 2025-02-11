#Working Data Types
print("1. Working with Data Types")
my_int = 25
my_float = 3.14
my_complex = 1 + 2j
my_str = "2nd year BSCpE"
my_list = [2, 4, 6, 8, 10]
my_tuple = (1, 3, 5, 7, 9)
my_set = {1,2,3}
my_frozenset = frozenset({4,5,6})
my_dict = {"name":"Clyde Drexler", "age": 25}
my_bool = True
my_none = None

#Printing Working with Data Types
print(type(my_int))
print(type(my_set))
print(type(my_str))
print(type(my_list))
print(type(my_tuple))
print(type(my_set))
print(type(my_frozenset))
print(type(my_dict))
print(type(my_bool))
print(type(my_none))

print("========================================================================================================")
print("2. Perform Operations on Data Types")
#Performing Operation and Data Types
#Arithmetic Operation
a = 25
b = 69

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")

#String Operations
text = "BSCpE"
print(f"Concatenation: {text + ' CPE 201'}")
print(f"Slicing: {text[:3]}")

#List And Set Operations
my_list.append(11)
my_set.add(4)
print(f"Updated List: {my_list}")
print(f"Updated Set:{my_set}")

#Dictionary Access
print(f"Dictionary Name: {my_dict['name']}")

print("========================================================================================================")
print("3. Using Operators")
#Using Operators with User Input
c = int(input("Enter first number: "))
d = int(input("Enter second number: "))

#Arithmetic Operation
print(f"Sum: {c + d}")
print(f"Difference: {c - d}")
print(f"Product: {c * d}")
print(f"Division: {c / d}")
print(f"Modulus: {c % d}")
print(f"Floor Division: {c // d}")
print(f"Exponentiation: {c ** d}")

#Comparison Operations
print(f"c == d: {c == d}")
print(f"c != d: {c != d}")
print(f"c > d: {c > d}")
print(f"c < d: {c < d}")
print(f"c >= b: {c >= b}")
print(f"c <= b: {c <= b}")

#Logical Operations
print(f"c and d: {c and d}")
print(f"c or d: {c or d}")
print(f"c not d: {not c}")

#Bitwise Operations
print(f"c & d: {c & d}")
print(f"c | b: {c | b}")
print(f"c ^ d: {c ^ d}")
print(f"~c: {~c}")
print(f"c << 1: {c << 1}")
print(f"c >> 1: {c >> 1}")