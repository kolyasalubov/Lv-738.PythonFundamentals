#-------------Calculate factorial of natural number, which will be entered by user, without using recurcion----------------

from math import factorial

# Getting value from user and checking if it's correct

while True:
    try:
        number = int(input("Please, enter natural number, which will be use to calculate factorial: "))
        if number < 1:
            raise ValueError
        break
    except ValueError:
        print("Please enter Int and Positive number")
    else:
        break

# Calculating factorial of entered number and printing result
print(f"Factorial of {number} is {factorial(number)}")