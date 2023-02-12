# Print all even numbers less than 100 (write two variants of the code:
# one using the while loop, and the other using the for loop).

number = 1

# while loop
while number < 100:
    if number%2 == 0:
        print(number)
    number += 1
    
# for loop
for number in range(100):
    if number%2 == 0:
        print(number)
    

## Print all odd numbers less than 100.
## (write two versions of the code: one using the continue operator, and
## the other without this operator). 

number = 1
    
## continue
for number in range(100):
    if number%2 == 0:
        continue
    print(number)

## without continue
for number in range(100):
    if number%2 == 1:
        print(number)


## Check if the list contains odd numbers. (Hint: use the break statement)

list = [34, 88, 96, 88, 33, 86, 100]

for a in list:
    if a%2 ==1:
        break

print(f"{a} is odd")
