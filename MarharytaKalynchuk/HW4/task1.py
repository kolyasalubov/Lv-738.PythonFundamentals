number = int(input('Please enter your number: '))
factorial = 1
while number>1:
    factorial=factorial*number
    number = number - 1

print(f'Factorial of the number is: {factorial}')