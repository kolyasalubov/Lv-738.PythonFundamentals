
class Employee:
    employee_number = 0
    empl_dict ={

    }


    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

        Employee.employee_number += 1
        Employee.empl_dict[f"{self._name}"] = self._salary

    @classmethod
    def total_num_of_empl(cls):
        print(Employee.employee_number)

    @staticmethod
    def all_empl_data():
        for empl in Employee.empl_dict:
            print(f"{empl}: {Employee.empl_dict[empl]}")


tom = Employee("Tom", 500)
cathy = Employee("Kate", 600)

Employee.total_num_of_empl()
Employee.all_empl_data()

