class TestError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)

def main_menu():
    while True:
        try:
            age = int(input("Please, enter your age in natural: "))
            check_age(age)
        except TestError as eroor:
            print(eroor)
        except ValueError as error:
            print("Error type: ", error)
        else:
            print(f"You are {age} years old")
            break

def check_age(age):
    if age <= 0: 
        raise TestError(f"You have entered negative age: {age}")
    if age > 120:
        raise TestError(f"You are too old, are you realy {age} years old?")
        

main_menu()