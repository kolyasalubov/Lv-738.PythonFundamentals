# Write a script that will check whether the entered number is even or odd and display the appropriate message.

num1 = int(input("num1: "))

if num1 % 2 != 0: 
  print(f"{num1} is odd")
else:
  print(f"{num1} is even")