password = input("Write your password")

while True:
    try:
        assert 6 <= len(password) <= 16
        assert any([i for i in password if i in "#$@"])
        assert any([i.isdigit() for i in password])
        assert any([i for i in password if i.isalpha() and i == i.upper()])
        assert any([i for i in password if i.isalpha() and i == i.lower()])
        print("Greetings! Wonderful password!")
        break
    except AssertionError:
        print("Too weak password. Try again!")
        password = input("Write your password")
    
