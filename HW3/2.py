n1 = input("enter a four-digit natural number: ")
n_list = list(n1)
n_list.reverse()
n2 = "".join(n_list)
print(f'write the number in reverse order: {"".join(n_list)}')
n_list.sort()
print(f'number in ascending order: {"".join(n_list)}')

