# Task1. Write a script that will calculate the factorial of the entered number without using recursion.

number = int(input("Please enter a number: "))

if number == 0:
    print(f"Impossible to calculate the factorial of the {number}") 
else:     
  factorial = 1
  for i in range(number):   
    factorial = factorial * (i + 1) 
  print(f"The factorial of the {number} is : {factorial}")