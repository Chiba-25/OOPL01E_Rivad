#Base Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        return f"Employee Name: {self.name}, Salary: ${self.salary}"

#Derived Classs (Inheritance)
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    #Overriding display_info method (Polymorphism)
    def display_info(self):
        return f"Manager Name: {self.name}, Salary: ${self.salary}, Department: {self.department}"

#Testing the Classes
employee = Employee("Seffhie Kean Duais", 50000)
manager = Manager("Francis Felismino", 10000, "IT")

print(employee.display_info()) #Calls method from Employee class
print(manager.display_info()) #Calls overridden method from Manager Class
