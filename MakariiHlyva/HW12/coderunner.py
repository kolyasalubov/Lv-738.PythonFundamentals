######### Task 1 - 1

# def add_tag(tag):
#     def decorator(func):
#         return tag + func() + tag
#     return decorator


# @add_tag("<strong>")
# def get_message():
#     return "Hello, World!" 

# print(get_message)

############## Task 1 - 2

# def first(func):
#     def inner():
#         return "123"+func()+"123"
#     return inner


# @first
# def burger():
#     return("-meat-")

# print(burger())


########## Task 2

# def celsius_to_fahrenheit(temps):
#     result = [item * 9 / 5 + 32 for item in temps]
#     return result



# celsius_temperatures = [0, 10, 20, 30, 40]
# print(celsius_to_fahrenheit(celsius_temperatures))
# # [32.0, 50.0, 68.0, 86.0, 104.0]
# celsius_temperatures = [-40, -30, -20, -10, 0]
# print(celsius_to_fahrenheit(celsius_temperatures))
# # [-40.0, -22.0, -4.0, 14.0, 32.0]

########### Task 3

# def fibonacci_numbers():
#     a, b = 0, 1
#     while 1:
#         yield a
#         a, b = b, a + b
    
    

# fib = fibonacci_numbers()
# for i in range(10):
#     print(next(fib))

########## Task 4

# def combinations(list1, list2):
#     for x in list1:
#         for y in list2:
#             yield (x, y)


# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# for combination in combinations(list1, list2):
#     print(combination)

########## Task 5

# def celsius_to_fahrenheit(temps):
#     return list(map(lambda x: x * 9/5 + 32, temps))


# celsius_temperatures = [0, 10, 20, 30, 40]
# print(celsius_to_fahrenheit(celsius_temperatures))
# # [32.0, 50.0, 68.0, 86.0, 104.0]
# celsius_temperatures = [-40, -30, -20, -10, 0]
# print(celsius_to_fahrenheit(celsius_temperatures))
# # [-40.0, -22.0, -4.0, 14.0, 32.0]

########### Task 6

# def celsius_to_fahrenheit(temps):
#     return list(map(lambda x: x * 9/5 + 32, temps))

# celsius_temperatures = [0, 10, 20, 30, 40]
# print(celsius_to_fahrenheit(celsius_temperatures))

# celsius_temperatures = [-40, -30, -20, -10, 0]
# print(celsius_to_fahrenheit(celsius_temperatures))