n = int(input("Enter a number: "))
a = 0
b = 1
for i in range(n):
    print(b, end=', ')
    a, b = b, a + b
    if b > n:
        break