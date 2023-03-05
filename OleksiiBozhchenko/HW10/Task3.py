# Task 3.
# Create an employee class. Each employee has characteristic such as name and salary.
#  The class should have a counter that calculates the total number of emplyee, as well as 
#  a method that prints the total number of employees and method that displays information 
#  about each employee in particular, namely the name and salary.
#  In addition to creating a class, display information about the base classes from wich the employee
#  class as inherited (__base__), the class namespace (__dict__), the class name (__name__), the module 
#  name in wich the class is defined (__module__), the documentation bar (__doc__)
class Employee():
    """
    Some text like a docstring for this class
    """
    
    count = 0 

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def __del__(self):
        Employee.count -= 1


    def counter():
        return print(Employee.count)

    def info(self):
        return print("Employee name: {}\nEmployee salary {}".format(self.name, self.salary))

    def class_info():
        print(Employee.__base__)
        print(Employee.__dict__)
        print(Employee.__name__)
        print(Employee.__module__)
        print(Employee.__doc__)


emp1 = Employee("Bob", 110)
emp2 = Employee("Ann", 120)
emp3 = Employee("Teddy", 130)

Employee.counter()
emp1.__class__.counter()

emp1.info()
# emp1.class_info()
Employee.class_info()

print(emp2)
print(isinstance (emp2, Employee))
del emp2
# print(isinstance(emp2, Employee))

Employee.counter()






