#3.3 Dictionaries
student_marks = {"John": 67, "Kate": 86, "Trevor": 92, "Jane": 55, "Anne": 79}
student_marks["Kate"] = 99  # Modifies Kate's value
student_marks["Matt"] = 76  # Adds a new key-value pair

print(student_marks.keys())   # Prints all keys
print(student_marks.values()) # Prints all values
print(student_marks.get("Kate"))  # Output: 99
print(student_marks.get("Marky")) # Output: None (does not raise an error)
