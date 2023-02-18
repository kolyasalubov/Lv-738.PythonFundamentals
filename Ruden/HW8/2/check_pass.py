import re


def check_password():
    while True:
        password = input("Enter password: ")
        if verification_password(password):
            print("Valid password!")
            break
        
        else:
            print('Invalid password. Try again.')


def verification_password(data):
    if not re.search('^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z$%#]{8,16}$', data):
        return False
    return True


