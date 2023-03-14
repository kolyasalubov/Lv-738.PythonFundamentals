#Task1

# try:
#     num = int(input("Please enter an integer: "))
#     if num%2 == 0:
#         print("Your number is even")
#     else:
#         print("Your number is odd")

# except ValueError as e:
#     print(f"Error {e}")


#Task2
try:
    number1, number2 = eval(input("Please enter two numbers with a comma: "))
    print(number1/number2)

except ZeroDivisionError as e:
    print(f"Error, {e}")
except SyntaxError as e:
    print(f"Error, {e}")
except ValueError as e:
    print(f"Error, {e}")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("Some message")

