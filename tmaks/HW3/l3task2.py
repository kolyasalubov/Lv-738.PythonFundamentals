import random

random_number = str(random.randint(1000, 9999))
l_numbers = []

for i in random_number:
    l_numbers.append(int(i))

l_numbers.sort()
print(sum(l_numbers))
print(random_number[::-1])
print(sorted(l_numbers))
