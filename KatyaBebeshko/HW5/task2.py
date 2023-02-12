# Task2. Create a list that contains elements of integer type,
# then use the loop to change the type of these elements to a floating type.
# (Hint: use the built-in float () function).


list = [34, 88, 96, 88, 33, 86, 100, 77, 44, 67]

for index in range(len(list)):   
    list[index] = float(list[index])
    
    # currentInt = list[index]
    # currentAsFloat = float(currentInt)
    # list[index] = currentAsFloat

print(list)