day = {1:"Monday",2:"Tuesday",3:"Wensday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}

try:
    day_number = int(input("Enter your number: "))
    if day_number > 8:
        raise ValueError
    elif day_number<0:
        raise ValueError
    elif day_number in day.keys():
        print(day.get(day_number))
except ValueError:
    print("Enter only number the number in range 1-7")