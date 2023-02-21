age = int(input("Enter your age: "))

def what_age(age):
    try:
        if age <0:
            raise ValueError
        elif age%2==0 :
            print(f"Your age {age} is odd")  
        elif age%2!=0 :
            print(f"Your age {age} is even")
    except ValueError :
        print("Imposible age")

what_age(age)