#-------------------Make some operations with int-type number--------------------------

# Getting value from user
while True:
    try:
        number = int(input("Please, enter the int-type number: "))
    except ValueError:
        print("Please enter correct number in int format")
        continue
    else:
        break

# Calculating the product of the digits of this number
number_in_str = str(number)
string_length = len(number_in_str)
result = int(number_in_str[0])

for counter in range(1, string_length):
    result *= int(number_in_str[counter])
print(f"Result of calculating the product of the digits of number {number} is: {result}")

# writing the number in reverse order
reversed_str = number_in_str[string_length-1]

for counter in range((string_length - 2), -1, -1):
    reversed_str += number_in_str[counter]
print(f"Result of writing the {number} in reverse order: {reversed_str}")

# Sorting characters in number in ascending order
sorted_chars = sorted(number_in_str)
sorted_number_in_string = ''.join(sorted_chars)
print(f"Result of sorting characters in number in ascending order of {number} is : {sorted_number_in_string}")