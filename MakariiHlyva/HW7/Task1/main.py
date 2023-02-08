#-------Function looks for bigest number of two numbers--------#


def largest_number(f_number, s_number):
    """This Function looks for bigest number of two numbers"""

    if f_number > s_number:
        print(f"{f_number} > {s_number}")
    elif f_number < s_number:
        print(f"{f_number} < {s_number}")
    else:
        print(f"{f_number} == {s_number}")


# Getting data from console

while True:
    try:
        f_number = float(input("Please enter firs number: "))
        break
    except ValueError:
        print("Argument, you are enterng should be a number, try again")
    else:
        break

while True:
    try:
        s_number = float(input("Please enter second number: "))
        break
    except ValueError:
        print("Argument, you are enterng should be a number, try again")
    else:
        break


# Calling function

print(largest_number.__doc__)
largest_number(f_number, s_number)
