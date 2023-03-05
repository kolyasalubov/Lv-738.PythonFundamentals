# def getProduct (num1):
#     product = 1
    
#     while (num1 != 0):
#         product = product * (num1 % 10)
#         num1 = num1 // 10
        
#     return product

# num1 = 5125

# print(getProduct(num1))

################################################

# def getProduct(n):
     
#     if(n == 0):
#         return 1
     
#     return (n%10) * getProduct(n//10) 
 
 
# print(getProduct(4567))

###################################################

# num2 = 4567

# print(str(num2)[::-1])

########################################

numbers = '34521'

print(sorted(numbers, reverse=False))