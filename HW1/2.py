what = input("Сhoose an action (+,-,/,*,**,//,%):")

a = float(input ("Enter the first number: "))
b = float(input("Enter the second number: "))

if what == "+":
    c = a + b
    print("Result" + str(c))
elif what == "-":
    c = a - b
    print("Result:" + str(c))
elif what == "/":
    c = a / b
    print("Result:" + str(c))
elif what == "*":
    c = a * b
    print("Result:" + str(c))
elif what == "**":
    c = a ** b
    print("Result:" + str(c))
elif what == "//":
    c = a // b
    print("Result:" + str(c))
elif what == "%":
    c = a % b
    print("Result:" + str(c))
else:
    print("Invalid operation selected")