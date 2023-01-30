# Task3. Print Fibonacci numbers up to the entered number n, using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

n = int(input("Enter a number: "))

if n>0 :
    print(0)
if n>1 :
    print(1)
else :
    exit

currentMinus2 = 0
currentMinus1 = 1
current = currentMinus2 + currentMinus1

while current < n:
    print(current)
    currentMinus2 = currentMinus1
    currentMinus1 = current
    current = currentMinus2 + currentMinus1
