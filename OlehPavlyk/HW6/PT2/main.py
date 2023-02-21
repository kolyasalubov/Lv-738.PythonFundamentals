flag = "False"
while flag == "False":
    user_name = input("enter the user name :")
    if user_name == "First":
        print("Congratulations!!! You have successfully logged in.")
        flag = "True"
    else:
        print("ERROR: User name is incorrect.\n Try again.")
