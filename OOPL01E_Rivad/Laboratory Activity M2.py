#Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

#Derived class: Student
class Student(Person):
    def __init__(self, name, age, grade_level):
        super().__init__(name, age)
        self.grade_level = grade_level

    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}, Grade Level: {self.grade_level}")

#Derived class: Teacher
class Teacher(Person):
    def __init__(self,name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        print(f"Teacher Name: {self.name}, Age: {self.age}, Subject: {self.subject}")

#Creating Objects
student = Student("Alice", 16, "10th Grade")
teacher = Teacher("Mr. John", 40, "Mathematics")

#Demonstrating Polymorphism
student.display_info()
teacher.display_info()