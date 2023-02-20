# Write a program that analyzes the entered number and, depending on the number, gives
# the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). Take
# into account cases of entering numbers from 8 and more, as well as cases of entering nonnumerical data.

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

try:
    day = input("Please enter the number from 1 to 7 : ")
    if day.lstrip("-").isdigit():
        day = int(day)
        if day not in range(1,8):
            raise ValueError("You entered a number outside the range from 1 to 7")
        else:
            print(week[day-1])
    else:
        raise ValueError("You entered a non-numeric value.")

except(ValueError, AttributeError) as e:
    print(f"Error : {e}")