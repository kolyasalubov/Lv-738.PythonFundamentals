import re 

password = input("Please enter your password: ")


regex_digits = "[0-9]"
regex_a_z = "[a-z]"
regex_A_Z = "[A-Z]"
regex_spec = "[$#@]"



match_digits = re.search(regex_digits, password)
match_a_z = re.search(regex_a_z, password)
match_A_Z = re.search(regex_A_Z, password)
match_spec = re.search(regex_spec, password)

if (
    match_digits != None and \
    match_a_z != None and \
    match_A_Z != None and \
    match_spec != None and\
    len(password) >= 6 and \
    len(password) <= 16
    ):
    print("Password is valid")
else:
    print('Please try again')


