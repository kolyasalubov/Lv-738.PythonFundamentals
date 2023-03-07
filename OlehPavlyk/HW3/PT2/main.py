import random

numeric = random.randint(1000, 9999)
print("The numeric is:", numeric)


def sorting(numer):
    array = list(numer)
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    return array


num = str(numeric)
first = int(num[0])
second = int(num[1])
third = int(num[2])
fourth = int(num[3])

reversed_num = "".join(reversed(num))  # не дуже зрозумів це


print("The product of the digits is:", first*second*third*fourth)
print("Revers numeric is :", reversed_num)
print("Numeric after sorting:", sorting(num))
