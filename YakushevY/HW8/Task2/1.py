import re



password = str(input("Create and enter your password: "))
condition1 = len(password)
condition2 = re.findall("[a-z]",password)
condition3 = re.findall("[A-Z]",password)
condition4 = re.findall("\d",password)
condition5 = re.findall("[$#@]",password)



if condition1 < 6:
    print("Minimum length 6 characters\nPlease follow these parameters when creating a password")
elif condition1 > 16:
    print("Maximum length 16 characters\nPlease follow these parameters when creating a password")
elif len(condition2)<=0:
    print("At least 1 letter between [a-z]\nPlease follow these parameters when creating a password")
elif len(condition3)<=0:
    print("At least 1 letter between [A-Z]\nPlease follow these parameters when creating a password")
elif len(condition4)<=0:
    print("At least 1 letter between [0-9]\nPlease follow these parameters when creating a password")
elif len(condition5)<=0:
    print("At least 1 letter between [$#@]\nPlease follow these parameters when creating a password")
else:
    print ("Your password created -",password)

