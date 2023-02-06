
user_login = "Login"
commit_log = False

while commit_log != True:
    answer = input("Enter login: ")
    if answer == user_login:
        print(f"Hello!!!")
        commit_log = True
    else:
        print(f"Error, wrong login! Please try again.")