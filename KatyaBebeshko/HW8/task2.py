# Task2.
# Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z]. At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

import re

## solution1

def passwordValidation(password):
    passwordLength = len(password)
    if passwordLength < 6 or passwordLength > 16:
        return False
    if not re.search("[a-z]",password) or not re.search("[A-Z]",password) or not re.search("[0-9]",password) or not re.search("[$#@]",password):
        return False
    return True

## solution2

def passwordValidationOnRegexp(password):
    return bool(re.match("(?=.*\d)(?=.*[$#@])(?=.*[a-z])(?=.*[A-Z]).{6,16}", password))
    



