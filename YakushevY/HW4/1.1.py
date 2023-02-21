def factorial(number):
    if number == 0:
        return 1
    else:
        return number*factorial(number-1)
number =int(input("Ener the number for the factorial: "))
print("Factorial of your number =" , factorial(number))
