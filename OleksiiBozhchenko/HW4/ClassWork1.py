# Write a script, which of the two entered numbers will determine which of them is more and which is less. 
# Take into account the case of equality of numbers.

num1 = int(input("num1: "))
num2 = int(input("num2: "))

if num1 > num2:
  print(f"{num1} bigger then {num2}")
elif num2 > num1:
  print(f"{num2} bigger then {num1}")
else:
  print(f"{num2} equals {num1}")