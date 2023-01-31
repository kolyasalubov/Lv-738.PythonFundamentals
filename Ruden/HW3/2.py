n1 = input("enter a four-digit natural number: ")
num_str = str(n1)
product = 1
for char in num_str:
        product = product * int(char)
print('product of digits: ', product) 
n_list = list(n1)
n_list.reverse()
n2 = "".join(n_list)
print(f'write the number in reverse order: {"".join(n_list)}')
n_list.sort()
print(f'number in ascending order: {"".join(n_list)}')

