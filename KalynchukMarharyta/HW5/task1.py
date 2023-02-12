ints = [2, 7, 9, 5, 7]
floats = []

for value in ints:
    floats.append(float(value))
print (floats)

#Using list comprehension
ints = [2, 7, 9, 5, 7]

floats = [float(x) for x in ints] 
print(floats)