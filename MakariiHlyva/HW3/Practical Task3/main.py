#----------------Interchange the values ​​of two variables without using the third variable-------------------

# Getting variables from user
variable_a = input("Please, enter first variable: a = ")
variable_b = input("Please, enter second variable b = ")

# Interchanging and printing the values of variables
variable_a, variable_b = variable_b, variable_a

print(f"Variable a = {variable_a}")
print(f"Variable b = {variable_b}")