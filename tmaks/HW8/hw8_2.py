import re

user_input = input("Create password: ")


if len(user_input) >= 6 and len(user_input) <= 16:
    for char in user_input:
        low_letter = re.findall("[a-z]", user_input)
        up_letter = re.findall("[A-Z]", user_input)
        spec_char = re.findall("[$#@]", user_input)
        num_char = re.findall("[\d]", user_input)

    if len(low_letter) == 0 or len(up_letter) == 0 or len(spec_char) == 0 or len(num_char) == 0:
        print("Invalid password")
    else:
        print(f"Your password is {user_input}")





