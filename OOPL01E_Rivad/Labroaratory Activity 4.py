class Student:
    def __init__(self, student_id, name, course, year_level):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.year_level = year_level

    def display_info(self):
        print(f'Student ID: {self.student_id}')
        print(f'Name: {self.name}')
        print(f'Course: {self.course}')
        print(f'Year Level: {self.year_level}')

# Instantiate three Student objects
student1 = Student(101, "Jaskaran Dhillon", "Mechanical Engineering", 2)
student2 = Student(102, "Cabanatan Cyrill", "Mechanical Engineering", 1)
student3 = Student(103, "Carl Godwill Marasignan Sescar", "Business Administration", 1)

# Display their information using the method
student1.display_info()
print("---------------")
student2.display_info()
print("---------------")
student3.display_info()
