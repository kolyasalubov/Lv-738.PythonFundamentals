#-------------Calculate Fibonacci numbers from entered number n-------------#

# Getting number n from user

while True:
    try:
        n = int(input("Please, enter number of Fibonacci numbers (Natural and Positive): "))
        if n < 1:
            raise ValueError
        break
    except ValueError:
        print("Please enter Int and Positive number")
    else:
        break

# Calculating Fibonacci numbers

match n:
    case 1:
        print("Your Fibonacci list is: [0]")
    case 2:
        print("Your Fibonacci list is: [0, 1]")
    case other:
        list_fibonacci = [int(0), int(1)]
        index = 2
        while index < n :
            list_fibonacci.append(list_fibonacci[index - 2] + list_fibonacci[index - 1])
            index += 1
        print("Your Fibonacci list is: ", list_fibonacci)
