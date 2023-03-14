##################

# names = ['Sam', 'Don', 'Daniel']

# # for i in range(len(names)):
# #     names[i] = hash(names[i])
# # print(names)

# hashnames = list(map(hash, names))
# print(hashnames)

##################

# Display a list of list items that have the values 
# "red", ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", “yellow”]
# using the filter function.

# list1 = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]
         
# new_1 = list(filter(lambda x: x == "red", list1))
# print(new_1)


##################

# listOfNumbers = ['1', '2', '3', '4', '5', '6', '7']

# new_list = list(map(int, listOfNumbers))
# print(new_list)

##################

listOfMiles = [45, 77, 44]

# listOfKM = list(map(lambda x: x*1.6, listOfMiles))
# print(listOfKM)

def convertMilesToKm(x):
    return x*1.6

print(list(map(convertMilesToKm, listOfMiles)))