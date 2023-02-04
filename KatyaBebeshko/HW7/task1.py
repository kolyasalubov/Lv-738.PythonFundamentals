## Task1. Write a function that returns the largest number of two numbers
## (use DocStrings documentation strings in the function).

def largestNumber(num1, num2):
    """
    This function return the 
    largest number of 2 numbers
    """
    if num1 > num2:
        return num1
    else:
        return num2

print(largestNumber(8, 8))