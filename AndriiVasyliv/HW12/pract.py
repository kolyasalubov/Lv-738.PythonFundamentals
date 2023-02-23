# names = ['Sam', 'Don', 'Daniel'] 

# # names_hash = list(map(lambda x: hash(x), names))

# names_hash = list(map(hash, names))
# print(names_hash)

#######################

# color = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]

# color_red1 = list(map(lambda n: n == "red", color))

# print(color_red1)

# color_red2 = list(filter(lambda n: n == "red", color))

# print(color_red2)

###########################

# a = ['1', '2', '3', '4', '5', '7']

# c = []
# for i in a:
#     return c == int(a)

# b = list(map(int, a))


# print(b)
# print(c)

#############################

# list1 = [1, 2, 3]

# c = list(map(lambda x, y: list1 * 1.6))

# pritn(c)


# for num in range(10, 14):
#    for i in range(2, num):
#        if num%i == 1:
#           print(num)
#           break




















# def count_vowels(word):
#     count = 0
#     i = 0  
#     for i in range(len(word)):
#         if (
#             (word[i] == "a")
#             or (word[i] == "e")
#             or (word[i] == "i")
#             or (word[i] == "o")
#             or (word[i] == "u")
#         ):
#             count += 1

#     return count

# print(count_vowels("dasdjk"))


# def mean(number):
#     sum = 0
#     count = len(str(number))
#     while (number !=0):
#         sum = sum + int(number % 10)
#         number = int(number/10)
        
#         averege = sum / count
        
#     return sum / count

# print(mean(55))

#######################################

# def decimal_to_binary(decimal_str):
#     decimal_num = int(decimal_str)
#     if decimal_num == 0:
#         return "0"
#     binary_str = ""
#     bit_value = 1
#     while bit_value <= decimal_num:
#         # Визначення значення поточного біту
#         bit = 1 if bit_value & decimal_num else 0
#         # Додавання біту до двійкового рядка
#         binary_str = str(bit) + binary_str
#         bit_value *= 2
#     return binary_str

# print(decimal_to_binary("10"))

###############################

# def isogram(string):
#     string = string.lower()
#     for  i in string:
#         if string.count(i) > 1:
#             return False
#     return True

# print(isogram("asd"))


################################
