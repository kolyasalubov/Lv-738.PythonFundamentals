# Create a list of integers that are entered from the terminal 
# and determine the maximum and minimum number among them.

a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
c = int(input('Enter number 3: '))

myList = [a, b, c]

print(f"Max value is {max(myList)}" )
print(f"Min value is {min(myList)}" )
