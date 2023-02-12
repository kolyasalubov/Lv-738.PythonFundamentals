# Write a function that returns the largest number of two nmbers
# (use DocStrings documentation strings in the function)
 
def compare(num1, num2):
    """
    This function compare two positive numbers and returns the largest one.
    If numbers are the same it return the negative value of the first parameter.
    """
    if num1 > num2:
        return num1
    elif num1 < num2:    
        return num2
    else:
        return num1 * -1

print(compare(24,45))
print(compare(5,5)) 

