number =int(input("Ener the number for the factorial: "))

i = 1
a = 1
b = 2

if number == 1 or number == 0:
    factorial = 1

while i < number:
    if number == 1 or number == 0:
        break
    else:
        factorial = a*b
        b=b+1
        a=factorial
        i += 1


print("Factorial of your number =" , factorial)
