# Task3. Create an employee class. Each employee has characteristics such as name
# and salary. The class should have a counter that calculates the total number of
# employees, as well as a method that prints the total number of employees and a
# method that displays information about each employee in particular, namely the
# name and salary.
# In addition to creating a class, display information about the base classes from which
# the employee class is inherited (__base__), the class namespace (__dict__), the
# class name (__name__), the module name in which the class is defined
# (__module__), the documentation bar ( __doc__)


class Employee():

    counter = 0 

    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary
        
    def totalEmployees():
        return Employee.counter

    def details(self):
        return f"Name: {self.name}, Salary {self.salary}"



empl1 = Employee("Katya", 3000)
empl2 = Employee("Anna", 4000)

print(Employee.totalEmployees())
print(Employee.details(empl1))
print(Employee.details(empl2))


print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
