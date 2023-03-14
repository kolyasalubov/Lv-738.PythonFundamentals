import re

def validate_password(password):
    while True:
        if len(password) < 6 or len(password) > 16:
            print("Your password is too short or too long. Try again.")
            password = input("Please enter your password: ")
            continue
        if not re.search("[a-z]", password):
            print("Your password does not contain any small letters! Try again.")
            password = input("Please enter your password: ")
            continue
        if not re.search("[A-Z]", password):
            print("Your password does not contain any capital letters! Try again.")
            password = input("Please enter your password: ")
            continue
        if not re.search("[0-9]", password):
            print("Your password does not contain any numbers! Try again.")
            password = input("Please enter your password: ")
            continue
        if not re.search("[@#$]", password):
            print("Your password does not contain any special symbols! Try again.")
            password = input("Please enter your password: ")
            continue
        
        print("Your password is ok!")
        break
    
password = input("Please enter your password: ")
validate_password(password)



