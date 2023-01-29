# Geting values of variables a and b from console and chacking if it's float
while True:
    try:
        a = float(input("Please enter value of varieble a:\n"))
        b = float(input("Please enter value of variable b:\n"))
    except ValueError:
        print("Please enter a correct values")
        continue
    else:
        break

# Printing resaults of different mathematic calculations
print("\"a + b = \"", a + b)
print("\n\"a - b = \"", a - b)
print("\n\"a * b = \"", a * b)
print("\n\"a / b = \"", a / b)
print("\n\"a**b = \"", a ** b)
print("\n\"a//b = \"", a // b)
print("\n\"a%b = \"", a % b)