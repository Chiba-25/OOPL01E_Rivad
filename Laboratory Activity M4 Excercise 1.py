#Excercise 1: Encapsulation - Student Grade Book

class Student:
    def __init__(self,name):
        self._name = name #private variables to store student name
        self._grades = [] #ricate list to store students grade

    def add_grade(self,grade): #adds a garde to the student's list of grade
        self._grades.append(grade)

    def get_average(self): #calculates the returns grades of the student
        if self._grades:
            return sum(self._grades) / len(self._grades)
        return 0
    def get_name(self): #returns the name of the student
        return self._name


#Example Usage
student = Student("Alice")
#Add grades to alice's record
student.add_grade(90)
student.add_grade(85)
student.add_grade(95)

#Output the student's name and average grade
print("Students Name: ", student.get_name())
print("Average Grade: ", student.get_average())