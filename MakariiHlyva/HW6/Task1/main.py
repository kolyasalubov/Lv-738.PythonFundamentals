#---------Check numbers from 1 to 10 and make a lists of numbers %2 == 0, %3 == 0 and (%2 and %3) != 0--------#

# function that will check a list of numbers

def check_numbers(check_list):
    even = []
    odd = []
    other = []
    for index in range (0, len(check_list), 1):
        if (check_list[index] % 2 != 0) and (check_list[index] % 3 != 0):
            other.append(check_list[index])
        if check_list[index] % 2 == 0:
            even.append(check_list[index])
        if check_list[index] % 2 != 0 and check_list[index] % 3 == 0:
            odd.append(check_list[index])
    return even, odd, other

check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even, odd, other = check_numbers(check_list)

#Printing results

print(f"Even numbers: {even}\nOdd numbers: {odd}\nOther numbers: {other}")