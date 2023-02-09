def solution(number):
    sum_multiples = 0
    for n in range(0, number):
        if n % 3 == 0 or n % 5 == 0:
            sum_multiples += n
    return sum_multiples



