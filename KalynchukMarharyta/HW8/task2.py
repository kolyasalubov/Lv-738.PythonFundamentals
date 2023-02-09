import re 

password = input("Please enter your password: ")


regex_digits = r"([0-9]+)"
regex_a_z = r"([a-z]+)"
regex_A_Z = r"([A-Z]+)"


match_digits = re.match(regex_digits, password)
match_a_z = re.match(regex_a_z, password)
match_A_Z = re.match(regex_A_Z, password)

if match_digits != None and match_a_z != None and match_A_Z != None:
    print("Password is valid")
else:
    print('Please try again')

# password = input('Please input your password: ')

# pattern = re.compile(r'[a-z]+')

# if pattern.fullmatch(password) is not None:
#     print('Found match ' + password)
# else:
#     print('No match')