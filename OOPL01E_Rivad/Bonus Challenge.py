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
