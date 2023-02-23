class Employee:

    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
        Employee.counter += 1

    def employees_counter():
        print(f'Total number of employees is {Employee.counter}')

    def employee_info(self):
        print(f'Employee name is {self.name}, employee salary is {self.salary}')
    
    def base_class_info():
        print(Employee.__mro__)
        print(Employee.__base__)
        print(Employee.__dict__)
        print(Employee.__name__)
        print(Employee.__module__)
        print(Employee.__doc__)
    

empl1 = Employee('Marharyta', 36)
empl2 = Employee('Sarah', 48)

Employee.employees_counter()

empl1.employee_info()

Employee.base_class_info()