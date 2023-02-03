#-------------Calculate factorial of natural number, which will be entered by user, without using recurcion----------------

# Getting value from user and checking if it's correct

while True:
    try:
        number = int(input("Please, enter natural number, which will be use to calculate factorial: "))
        if number < 1:
            raise ValueError
        break
    except ValueError:
        print("Please enter Int and Positive number")
    else:
        break

# Calculating factorial of entered number and printing result

match number:
    case 1:
        print(f"Factorial of {number} = {number}")
    case other:
        result = 1
        for counter in range(2, number + 1, 1):
            result *= counter
        print(f"Factorial of {number} = {result}")