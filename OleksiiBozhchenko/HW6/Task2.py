# Write a script that checks the login that the user enters.
# If the login is "First", then greet the user. 
# If the login is different, send error message.
# (need to use loop while) 

while True:
    login = str(input("Please enter the login: "))
    if login == str("First"):
        print(f"Hello {login}")
    else:
      print("Error, try again")
