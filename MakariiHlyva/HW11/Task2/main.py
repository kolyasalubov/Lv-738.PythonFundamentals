def main_menu():
    while True:
        try:
            day = int(input("Please, enter number od day from 1 to 7: "))
            check_data(day)
        except ValueError as error:
            print("Error: ", error)
        else:
            print(f"{day} day is a {days[day - 1]}")
            break

def check_data(day):
    if day > 7:
        raise ValueError(f"Are you crazy? Week doesn't have {day} days")
    elif day <= 0:
        raise ValueError(f"You have entered not positive number: {day}")



days = ['Monday', 'Thuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sanday']
main_menu()