

#--------- Using input -------------------
#------------ Def block ------------------


#def largest_numberV1(fst_num, sec_num):
#    """Returns largest number of two numbers. V1"""
#    if fst_num > sec_num:
#        return f"Biggest number is {fst_num}."
#    elif sec_num > fst_num:
#        return f"Biggest number is {sec_num}."
#    else:
#        return f"Numbers are equal."
#
#
#def largest_numberV2(num1, num2):
#    """Returns largest number of two numbers. V2 using max()"""
#    number_list = [num1, num2]
#    return f"Biggest is {max(number_list)}."
#
##-----------------------------------------
##------------- Run block -----------------
#
#
#first_number = int(input("Enter firs number: "))
#second_number = int(input("Enter second number: "))
#
#print(largest_numberV1(first_number, second_number))
#print(largest_numberV2(first_number, second_number))

#------------- Without using input -------

def largest_numberV1(fst_num, sec_num: int) -> str: # If just a number was returned: -> int
    """Returns largest number of two numbers. V1"""
    if fst_num > sec_num:
        return f"Biggest number is {fst_num}."
    elif sec_num > fst_num:
        return f"Biggest number is {sec_num}."
    else:
        return f"Numbers are equal."


def largest_numberV2(num1, num2: int) -> str: # If just a number was returned: -> int
    """Returns largest number of two numbers. V2 using max()"""
    number_list = [num1, num2]
    return f"Biggest is {max(number_list)}."


#------------- Run block ------------------

print(largest_numberV1(10, 5))
print(largest_numberV2(6, 19))
