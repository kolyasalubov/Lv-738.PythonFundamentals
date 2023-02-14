even_numbers_divisible_by_2 = []
odd_numbers_divisible_by_3 = []
numbers_not_divisible_by_2_and_3 = []
for i in range(1, 11):
    if i % 2 == 0:
        even_numbers_divisible_by_2.append(i)
    elif i % 3 == 0:
        odd_numbers_divisible_by_3.append(i)
    else:
        numbers_not_divisible_by_2_and_3.append(i)
print('Even numbers that are divisible by 2: ', even_numbers_divisible_by_2)
print('odd numbers, which are divisible by 3: ', odd_numbers_divisible_by_3)
print('numbers that are not divisible by 2 and 3: ', numbers_not_divisible_by_2_and_3) 
