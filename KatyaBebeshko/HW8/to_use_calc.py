import calculator as calc

action = int(input("Please enter the number of the action you want to perform: 1 - addition 2 - subtraction, 3 - multiplication 4 - division: "))

if action == 1:
    calc.addition(int(input("Enter 1st number: ")), int(input("Enter 2nd number: ")))

elif action == 2:
    calc.subtraction(int(input("Enter 1st number: ")), int(input("Enter 2nd number: ")))

elif action == 3:
    calc.multiplication(int(input("Enter 1st number: ")), int(input("Enter 2nd number: ")))

elif action == 4:
    calc.division(int(input("Enter 1st number: ")), int(input("Enter 2nd number: ")))

else:
    print("Wrong action.")