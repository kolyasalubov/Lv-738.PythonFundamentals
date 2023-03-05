# Write a program that analyzes the entered number and, depending on the number, gives 
# the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). Take 
# into account cases of entering numbers from 8 and more, as well as cases of entering non-numerical data

def day_of_week():
    try:  
        number = input('Please enter your number of day of week ')
        num_vs_day_dict = {'1': 'Monday', '2': 'Tuesday', '3': 'Wednesday', '4': 'Thursday', '5': 'Friday', '6': 'Saturday', '7': 'Sunday'}
        print(num_vs_day_dict[number])
    except KeyError:
            print('Value should be a number from 1 to 7')    

day_of_week()