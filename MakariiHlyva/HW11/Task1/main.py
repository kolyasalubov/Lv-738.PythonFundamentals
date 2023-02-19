def main_menu():
    while True:
        try:
            age = int(input("Please, enter your age in natural: "))
            check_age(age)
        except ValueError as error:
            print("Error type: ", error)
        else:
            print(f"You are {age} years old")
            break

def check_age(age):
    if age <= 0: 
        raise ValueError(f"You have entered negative age: {age}")
        

main_menu()