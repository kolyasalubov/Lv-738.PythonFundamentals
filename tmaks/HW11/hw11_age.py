

class CustomError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)



def even_odd_age(us_input):
    try:

        if us_input[0] == "-":
            raise CustomError("Number should be positive!")
        if int(us_input)%2 == 0:
            print("Your age is even")
        elif int(us_input)%2 != 0:
            print("Your age is odd")
    except CustomError as e:
        print(f"Error, {e.data}")
    except ValueError as e:
        print(f"Error, {e}")



user_input = input("Enter your age: ")

even_odd_age(user_input)

