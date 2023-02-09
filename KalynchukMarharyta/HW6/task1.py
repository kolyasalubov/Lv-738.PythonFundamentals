even_numbers = []
odd_numbers = []
numbers_not_div_2_3 = []


for number in range(1, 10):
    if number %2 == 0:
        even_numbers.append(number)
    elif number %2 != 0 and number %3 == 0:
        odd_numbers.append(number)
    else:
        numbers_not_div_2_3.append(number)

print(f'Even numbers divisible by 2: {even_numbers}')
print (f'Odd numbers divisible by 3: {odd_numbers}')
print(f'Numbers not divisible by 2 and 3: {numbers_not_div_2_3}')

#List comprehension:
l1 = [x for x in range(1,11) if x % 2 == 0]
l2 = [x for x in range(1,11) if x % 2 == 1 and x % 3 == 0]
l3 = [x for x in range(1,11) if not x % 2 == 0 and not x % 3 == 0]
print(l1, 'is an even multiple of 2')
print(l2, 'is an odd multiple of 3')
print(l3, 'is not divisible by 2 and 3')

