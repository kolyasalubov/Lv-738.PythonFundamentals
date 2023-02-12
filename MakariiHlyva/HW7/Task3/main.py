#--------calculate number of characters included in given string---------#

def make_list_from_str(check_str):
    """This function calculate number of characters included in given string"""

    str_list = list(check_str)
    res_dict = {}
    for index in range(0, len(str_list), 1):
        if str_list[index] not in res_dict:
            res_dict[str_list[index]] = str_list.count(str_list[index])
    
    print(res_dict)


check_str = str(input("Please enter the string which you want to ckeck: "))
print("\n", make_list_from_str.__doc__)
make_list_from_str(check_str)
