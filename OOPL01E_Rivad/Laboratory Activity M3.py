# Base Class
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print(f"[Employee] Name: {self.name}, ID: {self.employee_id}, Salary: ${self.salary}")


# Derived Class Manager
class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def display_info(self):
        print(f"[Manager] Name: {self.name}, ID: {self.employee_id}, Salary: ${self.salary}, Department: {self.department}")


# Derived Class Developer
class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def display_info(self):
        print(f"[Developer] Name: {self.name}, ID: {self.employee_id}, Salary: ${self.salary}, Programming Language: {self.programming_language}")


# Derived Class Intern
class Intern(Employee):
    def __init__(self, name, employee_id, salary, duration):
        super().__init__(name, employee_id, salary)
        self.duration = duration

    def display_info(self):
        print(f"[Intern] Name: {self.name}, ID: {self.employee_id}, Salary: ${self.salary}, Duration: {self.duration} months")


# Polymorphic Function
def show_employee_details(employee):
    if isinstance(employee, Intern):
        print("This is an intern with the following details:")
    employee.display_info()


# Create Employee Objects
manager = Manager(name="Alice", employee_id=101, salary=80000, department="HR")
developer = Developer(name="Bob", employee_id=102, salary=75000, programming_language="Python")
intern = Intern(name="Charlie", employee_id=103, salary=15000, duration=6)

# Store Employees in a List
employees = [manager, developer, intern]

# Iterate through Employees and Show Details
for employee in employees:
    show_employee_details(employee)
