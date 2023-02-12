def check_is_number(number, random_number, counter):
    try:
        if counter > 10:
            return f"You left {counter - 1}  hahaha you LOST luser "
        else:
            check = int(number)
            if type(check) is int and (check) >= 1 and check < 100:
                if check == random_number:
                    return "YOU WINN,YOU ARE CRAZY WIZARD"
                elif check > random_number:
                    return f"Your number({number}) is not corect and over, {10 - counter} tries left"
                elif check < random_number:
                    return f"Your number({number}) is not corect and less, {10 - counter} tries left"
            else:
                raise ValueError
    except ValueError:
        return f"Type {number} incorect have to be > 1 and < 100, {10 - counter} tries left"