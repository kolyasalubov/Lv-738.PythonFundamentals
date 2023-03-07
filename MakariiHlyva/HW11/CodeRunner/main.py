#------------------- CodeRunner Task 1------------------------#


# class InputError(Exception):
#     data = ''

# def check(text):
#         if type(text) is not str:
#             InputError.data = "Type text error"
#             raise InputError
#         elif len(text) < 3:
#             InputError.data = "Short text error"
#             raise InputError
#         elif len(text) > 15:
#             InputError.data = "Long text error"
#             raise InputError
#         else:
#             return True

# def test_input(text):
#     try:
#         print(check(text))
#     except InputError as e:
#         print(e.data)
        
# test_input("")
# test_input("Hello world")
# test_input("Long text that can not be placed in some document")
# test_input({})


#------------------------------ CodeRunner Task2 -----------------------------#


# def check_odd_even(number):
#     try:
#         if type(number) is not int:
#             raise ValueError("You entered not a number.")
#         elif number %2 == 0:
#             raise ValueError("Entered number is even")
#         elif number %2 != 0:
#             raise ValueError("Entered number is odd")

#     except ValueError as error:
#         return(error)


# print(check_odd_even(15))
# print(check_odd_even(-6))
# print(check_odd_even(0))
# print(check_odd_even("plp"))
# print(check_odd_even(36))


#------------------------------- CodeRunner Task3 -------------------------------#


# def divide(numerator, denominator):
#     try:
#         if type(numerator) is not int or type(numerator) is not int:
#             raise ValueError("Value Error! You did not enter a number!")
#         elif denominator == 0:
#             raise ValueError(f"Oops, {numerator}/{denominator}, division by zero is error!!!")
#         else:
#             return f"Result is {numerator / denominator}"

#     except ValueError as error:
#         return error
    
# print(divide(4, 8))
# print(divide(8, 0))
# print(divide("9", 3))


#-------------------------------- CodeRunner Task4 --------------------------------#


# class MyError(Exception):
#     pass

# def check_positive(number):
#     try:
#         if type(number) == str and not(number.isdigit()):
#             raise MyError("Error type: ValueError!")
#         if float(number) <= 0:
#             raise MyError(f"You input negative number: {float(number)}. Try again.")
#         elif float(number) > 0:
#             return f"You input positive number: {float(number)}"
        

#     except MyError as error:
#         return error
    

# print(check_positive(8.9))
# print(check_positive(-19))
# print(check_positive("abs"))
# print(check_positive("45"))


#--------------------------------- CodeRunner Task5 -----------------------------#

# from random import choices
# from string import ascii_letters, digits
# from re import match

# def check(login):
#     # type your code here

#     if match(r"^(([aA][dD][mM][iI][nN])|([eE][mM][pP][lL][oO][yY][eE]{2}))(-|([iI][dD])|-[iI][dD])[0-9]{1,}$", login):
#         return True
#     else:
#         raise ValueError(f"incorrect login '{login}'")
    

# correct_login = "employee-124"
# print(check(correct_login))

# incorrect_login = "incorrect_login"
# try:
#     print(check(incorrect_login))
# except ValueError:
#     print("Catched")




# test_strings = [
#     "ADMIN-ID124",
#     "admin-iD3457",
#     "AdMinid2",
#     "ADmin-569",
#     "employee-124",
#     "emPloyee-124",
#     "EMPLOYEE-4689",
#     "EMPLOYEE-4689"
# ]

# for string in test_strings:
#     try:
#         if check(string):
#             print("checked successfully")
#     except ValueError as e:
#         print(f"checked not successfully with {string}")


# letters_and_digits = choices(ascii_letters, k=5)
# letters_and_digits.extend(choices(digits, k=5))
# incorect_login = ''.join(letters_and_digits)
# try:
#     if check(incorect_login):
#         print("checked successfully")
# except ValueError as e:
#     print(str(e) == f"incorrect login '{incorect_login}'")


#-------------------------- CodeRunner Task6 ---------------------------#


# def check_age(age):
#     if age <= 0:
#         raise ValueError("Incorect age")
    
# indicator = True


# while indicator:
#     try:
#         age = int(input())
#         check_age(age)
#         print(age)
#         indicator = False
#     except ValueError as error:
#         pass


# try:
#     print("1")
#     result = function_sum(10,20)
#     print("2")
# except Exception:
#     print("3")
# finally:
#     print("4")


# def error_1():
#     raise ValueError
#     print("1")
#     return  "2"

# def print_1():
#     print("3")

# try:
#     print_1()
# except ValueError:
#     print("4")
# else:
#     print("5")
#     print(error_1())
# finally:
#     print("6")
# print("7")

m = [1,2,3,4,5]

try:
    print(m[5])
except Exception:
    print("sdf1")
except IndexError:
    print("sdfdsf")