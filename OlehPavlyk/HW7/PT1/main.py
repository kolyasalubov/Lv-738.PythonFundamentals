def which_more(num1, num2):
    """
    :param num1: int, input from user
    :param num2: int, input from user
    :return: int or string
    """
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "the numbers is similar"


num_a = int(input("write the first number: "))
num_b = int(input("write the second number: "))
print(which_more(num_a, num_b))
