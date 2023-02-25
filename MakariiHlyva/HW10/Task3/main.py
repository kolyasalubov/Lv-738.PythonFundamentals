from re import match

class totalEmployee():
    total_employe = 0
    
    def __init__(self, name, salary):
        totalEmployee.total_employe += 1
        self.name = name
        self.salary = salary

    def printInfoEmployee(self):
        print(f"{self.name} has salary - {self.salary}")

    def printInfoTotal(list_of_emp):
        for index in list_of_emp:
            print(f"{index.name} has salary {index.salary}")

    def printTotalQuantity():
        print(f"Total employee in this company {totalEmployee.total_employe}")


# Function to check entered name

def enter_name():                                                                                           
    
    while True:
        try:
            name = input("Please, enter your name, first letter have to be in upper case: ")
            if len(name) > 15:
                raise ValueError("Too long name")                                                   # if len(name) more than 15
            else:
                if check_name(name):                                                                # if name is real name :)
                    return name
                else:
                    raise ValueError("You have entered not letteres")
            break
        except ValueError as error:
            print(error)

# Function to check entered salary

def enter_salary():
    while True:
        try:
            salary = float(input("Please, enter sallary: "))
            if salary <= 0:                                                                         # if salary lower then 0
                raise ValueError("Salary have to be possitive")
            else:
                return salary                                                                       # if everycing is ok - return salary
            break
        except (TypeError, ValueError) as error:
            print(error)


def check_name(name):                                                                               # check name is correct before make class with this name
    if match(r"^[A-Z]{1}[a-z]{2,}$", name):
        return True
    else:
        return False


def add_new_employee():                                                                             # if you want to repeat adding new employee
    res = input("Do you want to add new employee? Press 'y' or 'Y': ")
    if res == 'Y' or res == 'y':
        return True
    else:
        return False


# def print_all_employee():
#     for emp in list_of_employee:
#         pr



def main_menu():                                                                                    # main menu
    add = True
    
    while add:
        name = enter_name()                                                                         # get name from console
        salary = enter_salary()                                                                     # get salary from console

        list_of_employee.append(totalEmployee(name, salary))                                        # add new object into list
        add = add_new_employee()                                                                    # repeat loop if we wants to add new employee
        

#----------------------------------------------main program----------------------------------------------#

list_of_employee = []

main_menu()
totalEmployee.printInfoTotal(list_of_employee)
totalEmployee.printTotalQuantity()



















# list_of_emp.append(totalEmployee('Stapan', 30))
# list_of_emp.append(totalEmployee('Ivan', 125))
# list_of_emp.append(totalEmployee('Mary', 12))



# print(list_of_emp[0].name, list_of_emp[0].salary)

