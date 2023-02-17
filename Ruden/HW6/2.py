correct_login = "First"

while True:
    login = input("Enter your login: ")
    if login == correct_login:
        print("Welcome ", login)
        break
    else:
        print("Incorrect login.")
        