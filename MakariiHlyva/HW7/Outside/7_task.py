#--------Multiples of 3 or 5-------#

def solution(number):
    sum = 0
    if number <= 0:
        return 0
    else:
        number -= 1
        while number != 0:
            if (number % 3 == 0) and (number % 5 == 0):
                sum += number
            elif number % 3 == 0:
                sum += number
            elif number % 5 == 0:
                sum += number
            number -= 1

        return sum

print(solution(4))
print(solution(6))
print(solution(16))
print(solution(3))
print(solution(5))
print(solution(15))
print(solution(0))
print(solution(-1))
print(solution(10))
print(solution(20))
print(solution(200))