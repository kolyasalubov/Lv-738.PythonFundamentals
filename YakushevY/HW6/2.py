while True:
    login = input("Ente your login: ")
    f = open("Lv-738.PythonFundamentals/YakushevY/HW6/1.txt","r")
    s = f.read()
    if login in s:
        print("This login already exist\nPleas enter another login ")
    else:
        f = open("Lv-738.PythonFundamentals/YakushevY/HW6/1.txt","a+")
        f.writelines(login + "\n")
        print("Congratulations, your login register")
        break

