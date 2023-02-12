import operations

while True:
    action = input("Enter action type +, -, *, / or Q for quit: ")
    match action:
        case "Q" | "q":
            break
        case _:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            match action:
                case "+":
                    print(operations.sum(num1,num2))
                case "-":
                    print(operations.difference(num1,num2))
                case "*":
                    print(operations.product(num1,num2))
                case "/":
                    print(operations.division(num1,num2))
                case _:
                    print("Something get wrong. Try again.")
                    continue
                    

            