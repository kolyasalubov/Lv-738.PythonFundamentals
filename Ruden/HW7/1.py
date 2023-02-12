def returns_largest_number(num1, num2):
    """
    Function that returns the largest number of two numbers
    """
    if num1 == num2:
        return ("You can't compare the same numbers")
    else:
        return num1 if num1 > num2 else num2
    #return num1 if num1 > num2 else num2
print(returns_largest_number(2, 2))