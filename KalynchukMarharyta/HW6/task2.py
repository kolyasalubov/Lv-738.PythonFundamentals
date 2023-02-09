# login = input('Please enter your login: ')

# while login != 'First':
#     login = input('Error! Please enter your login again: ')
# else:
#     print(f'Greeting, {login}!')

lst = [0, 0, 0, 0, 0]
def add_indexes(lst):
    index_sum_list = []
    for i in lst:
        print(lst.index(i))
        index_sum_list.append(i+lst.index(i))
    return index_sum_list

a = add_indexes(lst)
print(a)