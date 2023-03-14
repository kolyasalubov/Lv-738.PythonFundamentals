# Task1
names = ["sam", "don", "john"]

hashed_names = list(map(lambda x: hash(x), names))
print(hashed_names)

hashed_names = list(map(hash, names))
print(hashed_names)

# Task2
color = ["red", "green", "black", "red", "brown", "red", "blue","red", "red", "yellow"]
my_filter = list(filter(lambda x : x == "red", color))
print(my_filter)

my_map = list(map(lambda x : x == "red", color))
print(my_map)

# Task3
list1 = ["1", "2", "3"]
int1 = list(map(int, list1))
print(int1)

int2 = []
for i in list1:
  print(i)
  int2.append(int(i))
print(int2)

# Task4
list2 = [2,4,6]
print(list(map(lambda x : x*1.6, list2)))

def ff1(x):
  return x * 1.6
print(list(map(ff1, list2)))