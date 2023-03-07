list1 = []
for i in range(1, 11):
    list1.append(i)
print(f"origin list {list1}")
print("even numbers which divisible by 2: ", end="")
t = 0
for t in range(len(list1)):
    if list1[t] % 2 == 0:
        print(list1[t], end=", ")
print("\nOdd numbers which divisible by 3: ", end="")
for t in range(len(list1)):
    if list1[t] % 2 == 1:
        if list1[t] % 3 == 0:
            print(list1[t], end=", ")
print("\nNumbers which are not divisible by 2 and 3: ", end="")
for t in range(len(list1)):
    if list1[t] % 2 == 1:
        if list1[t] % 3 == 1 or list1[t] % 3 == 2:
            print(list1[t], end=", ")
print(".")
