############ Task1

# names = ['Sam', 'Don', 'Daniel']
# result = list(map(lambda item: hash(item), names))

# print(result)

############ Task 2

# inp = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]

# res = list(filter(lambda item: item == "red", inp))

# print(res)

############ Task 3

# inp = ['1', '2', '3', '4', '5', '7']

# res = []
# for index in inp:
#     res.append(int(index))

# print(res)

# res2 = list(map(lambda i: int(i), inp))

# print(res2)

############# Task 4

# input = [10, 20, 30, 40]

# def km_to_m(km):
#     return km * 1.6

# res1 = list(map(km_to_m, input))
# res2 = list(map(lambda km: km * 1.6, input))

# print(res1)
# print(res2)

############## Task 5

# from functools import reduce

# inp = [1, 20, 30, 50]
# res = reduce(lambda x, y: x if x > y else y, inp)
# print(res)

############## Task 6

# def test_gen():
#     for i in range(0, 10):
#         yield i

# for el in test_gen():
#     print(el)

# def first(func):
#     def inner():
#         print("<\ ^^^^^^^ />")
#         func()
#         print("<\ ______ />")
#     return inner

# def second(func):
#     def inner():
#         print("# tomato #")
#         func()
#         print("~ salad ~")
#     return inner

# @first
# @second
# def burger():
#     print("-meat-")

# print(burger())

def first(func):
    def inner():
        return "123"+func()+"123"
    return inner


@first
def burger():
    return("-meat-")

print(burger())