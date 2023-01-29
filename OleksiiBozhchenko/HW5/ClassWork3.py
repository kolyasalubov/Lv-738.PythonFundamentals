# #

# for i in [32, 35, 71]:
#   if i%2 == 1:
#     print(i)
#     break

# Create a list of integers that are entered from the terminal and determine the maximum and minimum number among them.

# i = list(input("Enter some numbers separated by comma : ").split(","))
# print("Min value is - " + min(i) + ". Max value is - " + max(i))

lst1=[]
for i in input().split():
    lst1.append(i)
print("Min value is - " + min(lst1) + ". Max value is - " + max(lst1))


#print(dir(list))

# 2:01:01 list comprehension
