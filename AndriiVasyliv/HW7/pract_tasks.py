# 1 Jenny's secret message

# def greet_user(name):
#     if name and name.strip().lower() == 'johnny':
#         return 'Hello, my love!'
#     else:
#         return 'Hello, {}!'.format(name)
# print(greet_user("Mary"))

# 2 Simple: Find The Distance Between Two Points

# import math

# def calculate_distance(p1, p2):
#     x1, y1 = p1
#     x2, y2 = p2
#     distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#     return round(distance, 2)

# print(calculate_distance((1, 0), (4, 0)))

# 3 No yelling!

# def filter_words(s):
#     words = s.split()
#     return ' '.join([words[0].title()] + [word.lower() for word in words[1:]]) + '.'
# print(filter_words('HELLO CAN YOU HEAR ME')) 
# print(filter_words('now THIS is REALLY interesting')) 
# print(filter_words('THAT was EXTRAORDINARY!')) 

# 4 Convert a Number to a String!

# def number_to_string(num):
#     return  str(num)

# print(number_to_string(123))
# print(number_to_string(-12))

# 5 Reversing Words in a String

# def reverse_words(s):
#     words = s.strip().split()
#     return ' '.join(words[::-1])

# print(reverse_words("Hello World"))

# 6 Reverse List Order

# def reverse_list(lst):
#     return lst[::-1]

# print(reverse_list([1, 2, 3, 4]))

# 7 Multiples of 3 or 5

# def sum_multiples(number):
#     if number < 0:
#         return 0
#     else:
#         return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
# print(sum_multiples(10))

# 8 Will you make it?

# def can_get_to_pump(distance_to_pump, mpg, fuel_left):
#     return True if distance_to_pump / mpg <= fuel_left else False
# print(can_get_to_pump(50, 25, 2))
# print(can_get_to_pump(67, 15, 4))

# 9 Are You Playing Banjo?

# def are_you_playing_banjo(name):
#     if name[0].lower() == 'r':
#         return name + " plays banjo"
#     else:
#         return name + " does not play banjo"

# print(are_you_playing_banjo("Rocco")) 
# print(are_you_playing_banjo("Ann"))

# 10 Convert boolean values to strings 'Yes' or 'No'

# def bool_to_word(boolean):
#     if boolean:
#         return "Yes"
#     else:
#         return "No"
# print(bool_to_word(True))
# print(bool_to_word(False))

# 11 Counting sheep...

# def count_sheep(sheep_list):
#     count = sheep_list.count(True)
#     return count

# print(count_sheep([True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]))

# 12 Is this my tail?

def correct_tail(body, tail):
    return body.endswith(tail)
print(correct_tail("Snake","e"))
print(correct_tail("Mouse","f"))
