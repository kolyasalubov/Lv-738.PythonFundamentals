# Write a program that analyzes the entered number and, depending on the number, gives
# the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). Take
# into account cases of entering numbers from 8 and more, as well as cases of entering non-
# numerical data.

def analyzeDay(userInput):
    try:
        weekDay = int(userInput)
        match weekDay:
            case 1:
                print("Today is Monday")
            case 2:
                print("Today is Tuesday")
            case 3:
                print("Today is Wednesday")
            case 4:
                print("Today is Thursday")
            case 5:
                print("Today is Friday")
            case 6:
                print("Today is Saturday")
            case 7:
                print("Today is Sunday")
            case _:
                print("Value is not from 1 to 7")

    except ValueError as e:
        print("Wrong input:", e)

userInput = input("Enter a number from 1 to 7: ")
analyzeDay(userInput)