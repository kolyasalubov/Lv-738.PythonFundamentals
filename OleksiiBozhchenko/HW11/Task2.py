#   Write a program that prompts the user to enter their age, and then displays a
# message stating whether the age is even or odd. The program must provide the ability
# to enter a negative number, and in this case generate an exception. The master code
# should call a function that processes the information entered.

def check(age):
    if age.lstrip("-").isdigit():
        age = int(age)
        if age <= 0:
            raise ValueError("Negative or Zero value")
        elif age % 2 == 0:
            print("Even")
        else:
            print("Odd")
    else:
        raise ValueError("Not a numeric value")

try:
    age = input("Enter your age : ")
    check(age)
except(ValueError) as e:
    print(f"Error : {e}")