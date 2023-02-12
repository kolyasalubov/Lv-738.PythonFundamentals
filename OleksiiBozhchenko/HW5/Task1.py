# Create a list that contains elements of integer type, 
# then use loop to change the type of these elements to a floating type
# (Hint: use the built-in float() function)

# # 
# #  Example 1
# # 
lst = [2,34,23,867,433,32]
for i in range(len(lst)):
    lst[i] = float(lst[i])
print(lst)

# # 
# #  Example 2
# # 
lst = [2,34,23,867,433,32]
count = 0
while count < (len(lst)):
    lst[count] = float(lst[count])
    count +=1
print(lst)