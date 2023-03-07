
class CustomError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


def day_func(numb):
    days_of_week = {
        "Monday": 1, "Tuesday": 2, "Wednesday": 3,
        "Thursday": 4, "Friday": 5, "Saturday": 6,
        "Sunday": 7,
    }

    try:
        user_number = int(numb)
        if user_number <= 0 or user_number > 7:
            raise CustomError("Number should be positive and be between 1 to 7.")
        for elem in days_of_week:
            if days_of_week[elem] == user_number:
                print(f"{elem}")


    except CustomError as e:
        print(f"Error, {e.data}")
    except ValueError as e:
        print(f"Error, {e}")

user_input = input("Enter a number: ")
day_func(user_input)