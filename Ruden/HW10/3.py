class Employee:
    """class to record the number of employees and their salaries"""
    employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employees += 1

    def display_employee_info(self):
        print(f"Employee name: {self.name}\nEmployee salary: {self.salary}\n")

    @classmethod
    def display_employees(cls):
        print(f"The number of employees: {cls.employees}\n")

# example usage
employee1 = Employee("Max", 5340)
employee2 = Employee("Ivan", 4214)

Employee.display_employees()

employee1.display_employee_info()
employee2.display_employee_info()


print(f'{Employee.__bases__} \n')  
print(f'{Employee.__dict__} \n')  
print(f'{Employee.__name__} \n')  
print(f'{Employee.__module__} \n')  
print(f'{Employee.__doc__} \n')  