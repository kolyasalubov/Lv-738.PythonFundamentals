#---------------Make list of integer numbers and after chenge type of all elements by loop----------------#


# Getting size of list from user

while True:
    try:
        list_size = int(input("Please, enter size of list (Natural): "))
        if list_size < 1:
            raise ValueError
        break
    except ValueError:
        print("Please enter Int and Positive number")
    else:
        break

# Making list from user entered values in terminal

list_of_integer = []
for index in range(0, list_size, 1):
    while True:
        try:
            value = int(input(f"Please enter values of {index + 1} element: "))
            list_of_integer.append(value)
            break
        except ValueError:
            print("Please enter Int and Positive number")
        else:
            break
print(f"Here is your list: \n", list_of_integer)

# Changing type of all elements into float

for index in range(0, list_size, 1):
    list_of_integer[index] = float(list_of_integer[index])