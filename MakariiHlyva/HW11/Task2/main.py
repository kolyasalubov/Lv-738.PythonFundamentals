class DaysError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


def main_menu():
    while True:
        try:
            day = int(input("Please, enter number od day from 1 to 7: "))
            check_data(day)
        except DaysError as eroor:
            print(eroor)
        except ValueError as error:
            print("Error: ", error)
        else:
            print(f"{day} day is a {days[day - 1]}")
            break

def check_data(day):
    if day > 7:
        raise DaysError(f"Are you crazy? Week doesn't have {day} days")
    elif day <= 0:
        raise DaysError(f"You have entered not positive number: {day}")



days = ['Monday', 'Thuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sanday']
main_menu()