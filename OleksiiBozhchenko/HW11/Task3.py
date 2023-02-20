# Write a program to calculate the divide of two numbers entered by the user
# sequentially through a comma, to predict the case of division by zero, cases of
# syntactic errors and cases of other exceptional situations. Use the else and finally
# blocks

try:
    a,b = input("Enter two numbers separated by a comma: ").split(",")
    res = int(a)/int(b)
except(ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
else:
    print(res)
finally:
    print("The programm was finished.")