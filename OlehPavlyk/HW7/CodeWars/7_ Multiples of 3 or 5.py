def solution(number):
    counter = 0
    if number < 0:
        number = 0
        return number
    else:
        for i in range(number):
            if i % 3 == 0 or i % 5 == 0:
                counter += i
    return counter
