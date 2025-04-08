#3.2 Tuples
my_tuple = (2, 5, 7, 23, 1)
try:
    my_tuple[2] = 5000  # This will raise an error
except TypeError as e:
    print(e)  # Explanation: Tuples are immutable
