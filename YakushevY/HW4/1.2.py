number =int(input("Ener the number for the factorial: "))

i = 1
a = 1
b = 2

while i < number:
    c = a*b
    b=b+1
    a=c
    i += 1

print("Factorial of your number =" , c)
