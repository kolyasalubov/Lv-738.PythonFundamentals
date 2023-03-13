######## EVEN NUMBERS
# for num in range(1, 11):
#     if num % 2 == 0:
#         print(num)
        
######## ODD NUMBERS

# for num in range(0, 11):
#     if num % 2 == 1 and num % 3 == 0:
#         print(num)

########### NOT %2 and %3

for num in range(0, 11):
    if num % 3 != 0 and num % 2 != 0:
        print(num)