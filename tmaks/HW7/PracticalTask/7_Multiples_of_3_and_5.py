
def solution(number):
    num_list = []
    for num in range(1, number):
        if num % 5 == 0 and num % 3 == 0:
            num_list.append(num)
        elif num % 3 == 0:
            num_list.append(num)
        elif num % 5 == 0:
            num_list.append(num)
    return sum(num_list)
