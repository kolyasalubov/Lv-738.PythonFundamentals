import random
ints = []
for i in range(random.randint(2, 15)):
    ints.append(random.randint(0, 100))
floats = [float(x) for x in ints]
print(floats)
