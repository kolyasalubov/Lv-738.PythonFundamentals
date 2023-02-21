def check_is_number(text_to_check, random_number, counter):
    try:
        if counter > 10:
            return f"You left {counter - 1} tries, you LOST :) HA-HA"
        else:
            check = int(text_to_check)
            if type(check) is int and (check) >= 1 and check < 100:
                if check == random_number:
                    return "YOU WINN"
                elif check > random_number:
                    return f"Your {text_to_check} is over, {10 - counter} tries left"
                elif check < random_number:
                    return f"Your {text_to_check} is less, {10 - counter} tries left"
            else:
                raise ValueError
    except ValueError:
        return f"Type {text_to_check} incorect have to be > 1 and < 100, {10 - counter} tries left"
