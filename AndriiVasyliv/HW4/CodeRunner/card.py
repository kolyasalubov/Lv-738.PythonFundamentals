# Write a function that takes a credit card number and only displays the last four characters. 
# The rest of the card number must be replaced by ************

# def card_hide(card):
    
#     card_max = "1231123412341234"
#     if len(card) < len(card_max):
#         return "Invalid card"
    
#     else:
#         return card.replace(card[0:12], "************")
    
# def divisible_by_five(number):
#     if number%5 == 0:
#         return True
    
#     return False

# print(divisible_by_five(1))

#################################

# from math import pi
# class Circle:
#     def __init__(self, r):
#         self.r = r
        
#     def getPerimeter(self):
#         return 2*pi*self.r

# circy = Circle(4.44)
# print(circy.getPerimeter())

###################################

# class parent:
#     def __init__(self, param):
#         self.v1 = param
        
# class child(parent):
#     def __init__(self, param):
#         self.v2 = param

# obj = child(11)

# print(obj.v1 + "" + obj.v2)

##################################

# aList = [1, 2]
# bList = [3, 4]

# kvps = {'1': aList, '2': bList}
# theCopy = kvps.copy()

# kvps['1'][0] = 5
# sum = kvps['1'][0] + theCopy['1'][0]
# print(sum)

##############################

# names = ['Amir', 'Barry', 'Chales', 'Dao']
# print(names[-1][-1])

#####################

# a = {}
# a[(1,2,4)] = 8
# a[(4,2,1)] = 10
# a[(1,2)] = 12
# sum = 0
# for k in a:
#     sum+= a[k]
    
# print(len(a)+ sum)

# def makes10(num1, num2):
#     if num1 == 10 or num2 == 10 or num1 + num2 == 10:
#         return True
#     else:
#         return False

# print(makes10(2, 2))


def fibo_element(n):
    if n in (1,2):
        return 1
    return fibo_element(n-1) + fibo_element(n-2)

print(fibo_element(6))