# Task1. Write a script that will calculate the factorial
# of the entered number without using recursion.
def taskOne():
    number1 = int(input("Number 1 is: "))


    if number1 < 0:
        print('Enter positive value.')
    else:
        factorialValue = 1
        while number1 > 1:
            factorialValue *= number1
            number1 -= 1

        print(factorialValue)

taskOne()

