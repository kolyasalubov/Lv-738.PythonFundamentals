from re import search

def enter_password():
    while True:
        try:
            password = str(input("Please enter the password, you want to create: "))
            if check_pass(password):
                print("You have sгccessfully create password")
            else:
                raise ValueError
            break
        except ValueError:
            print("Try again\n")

def check_pass(str):
    if len(str) >= 6 and len(str) <= 16:
        if search("[a-z]{1,}", str) and ("[A-Z]{1,}", str):
            if search("[0-9]{1,}", str):
                if search("[$#@]{1,}", str):
                    return True
                else:
                    print("Password does't have enought special character")
                    return False
            else:
                print("Password doesn't have enought numbers")
                return False
        else:
            print("Password doesn't have enought small or big letters")
            return False
    else:
        print('Pawwrod is too short or too long')
        return False