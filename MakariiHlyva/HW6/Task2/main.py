#---------Check user entered login----------#

# Using loop while until user will enter correct login

while True:
    try:
        login = input("Please, enter your login: ")
        if login == "First":
            print(f"Hello {login}")
        else:
            raise ValueError
        break
    except ValueError:
        print(f"Sorry, we can't find login {login}")
    else:
        break
