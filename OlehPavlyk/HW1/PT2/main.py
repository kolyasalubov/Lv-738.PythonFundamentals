print("choose the number of action")
action = input("1:'a + b' \n2:'a - b' \n3:'a * b' \n4:'a / b' \n5:'a**b' \n6:'a//b'\n7:'a%b'\nYour choice: ")
first_number = int(input("write the first number"))
second_number = int(input("write the second number"))


if action == "1":
    print("answer: ", first_number + second_number)

elif action == "2":
    print("answer: ", first_number - second_number)

elif action == "3":
    print("answer: ", first_number * second_number)

elif action == "4":
    if first_number | second_number != 0:
        print("answer: ", first_number / second_number)
    else:
        print("write the correct numbers!")

elif action == "5":
    print("answer: ", first_number ** second_number)

elif action == "6":
    if first_number | second_number != 0:
        print("answer: ", first_number // second_number)
    else:
        print("write the correct numbers!")

elif action == "7":
    print("answer: ", first_number % second_number)

else:
    print("Your choice isn`t correct, try again")
