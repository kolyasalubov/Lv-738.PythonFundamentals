n = int(input('Enter number: '))
factorial = 1
while n > 1:
    factorial = factorial * n
    n = n - 1
print('Factorial ', factorial)