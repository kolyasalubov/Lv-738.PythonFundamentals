str = input('Print your string: ')

result = {}
for keys in str:
    result[keys] = result.get(keys, 0) + 1

print(result)

