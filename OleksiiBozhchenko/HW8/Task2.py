# Task 2.
# Write a Python program to check the validity of a password(input from user).
# Validation:
# At least 1 letter between [a-z] and 1 letter between [A-Z]
# At least 1 number between [0-9]
# At least 1 character from [@#$]
# Minimum length 6 characters
# Maximum length 16 characters

import re

set_full = "^[a-zA-Z0-9!%^&*()_=+`~,<.>?[|$#@/\]\\\"\-\{\}]+$" # regex contains any numbers, letters and special symbols
set_pass = "^[a-zA-Z0-9$#@]+$" # regex contains full right set of numbers, letters and special symbols
set_nonumbers = "^[a-zA-Z$#@]+$" # regex contains right set of letters and special symbols w/o numbers
set_noupper = "^[a-z0-9$#@]+$" # regex contains right set of numbers, letters and special symbols w/o [A-Z]
set_nolower = "^[A-Z0-9$#@]+$" # regex contains right set of numbers, letters and special symbols w/o [a-z]
set_nosymbols = "^[a-zA-Z0-9]+$" # regex contains right set of numbers and letters w/o special symbols
while True:
    passwd = str(input("Please enter your password : "))
    if len(passwd) < 6:
        print("Your password is too short. Try again.")
        continue
    if len(passwd) > 16:
        print("Your password is too long. Try again.")
        continue
    pattern = re.compile(set_nonumbers)
    if pattern.search(passwd):
        print("Your password does not contain any numbers! Try again. ")
        continue
    pattern = re.compile(set_noupper)
    if pattern.search(passwd):
        print("Your password does not contain any capital letters! Try again. ")
        continue
    pattern = re.compile(set_nolower)
    if pattern.search(passwd):
        print("Your password does not contain any small letters! Try again. ")
        continue
    pattern = re.compile(set_nosymbols)
    if pattern.search(passwd):
        print("Your password does not contain any special symbols! Try again. ")
        continue
    pattern = re.compile(set_pass)
    if pattern.search(passwd):
        print("Your passord is OK!")
        break
    pattern = re.compile(set_full)
    if pattern.search(passwd):
        print("Your password contain wrong special symbols! Try again. ")
        continue
