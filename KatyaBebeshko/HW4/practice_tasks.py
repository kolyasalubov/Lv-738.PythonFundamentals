# Task2. Write a script, which of the two entered numbers will determine which of them is more
# and which is less. Take into account the case of equality of numbers.
def taskTwo():
    number1 = int(input("Number 1 is: "))
    number2 = int(input("Number 2 is: "))

    if number1 > number2:
        print("Number 1 is greater than number 2")
    elif number1 == number2:
        print("Number 1 equals number 2")
    else:
        print("Number 1 is less than number 2")

# Task3. Write a script that will check whether the entered number is even or odd
# and display the appropriate message.
def taskThree():
    number1 = int(input("Number 1 is: "))

    if number1%2 == 0:
        print("Number 1 is even")
    else:
        print("Number 1 is odd")


taskTwo()
# taskThree()
