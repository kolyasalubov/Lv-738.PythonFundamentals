# 2. Write a program that prompts the user to enter their age, and then displays a
# message stating whether the age is even or odd. The program must provide the ability
# to enter a negative number, and in this case generate an exception. The master code
# should call a function that processes the information entered.

class CustomError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return self.data

def analyzeAge(age):
    try:
        if age%2==0 and age>0:
            print("Your age is even")
        elif age < 1:
            raise CustomError("Your age can't be negative")
        else:
            print("Your age is odd")

    except CustomError as e:
        print("We obtain error:", e)

ageInput = int(input("Enter your age: "))
analyzeAge(ageInput)