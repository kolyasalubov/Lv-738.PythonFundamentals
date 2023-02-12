# Task 1
# DESCRIPTION:
# Jenny has written a function that returns a greeting for a user. 
# However, she's in love with Johnny, and would like to greet him slightly different. 
# She added a special case to her function, but she made a mistake.
def greet(name):
    if name == "Johnny":
      return "Hello, my love!"
    else:
      return "Hello, {name}!".format(name=name)
print(greet("any"))  

# Task 2
# DESCRIPTION:
# Given two ordered pairs calculate the distance between them. 
# Round to two decimal places. This should be easy to do in 0(1) timing.
from math import sqrt
def distance(x1, y1, x2, y2):
    return round(sqrt((x2 - x1)**2 + (y2 - y1)**2),2)
print(distance(1,1,0,0))


# Task 3
# DESCRIPTION:
# Write a function taking in a string like WOW this is REALLY          amazing and returning Wow this is really amazing. 
# String should be capitalized and properly spaced. Using re and string is not allowed.
# Examples:
# filter_words('HELLO CAN YOU HEAR ME') #=> Hello can you hear me
# filter_words('now THIS is REALLY interesting') #=> Now this is really interesting
# filter_words('THAT was EXTRAORDINARY!') #=> That was extraordinary!
def filter_words(st):
    while "  " in st:
      st = st.replace("  ", " ")
    return st.capitalize().strip()
print(filter_words("HELLO CAN YOU HEAR ME"))
print(filter_words("now THIS is REALLY interesting"))
print(filter_words("THAT was           EXTRAORDINARY!  "))


# Task4
# DESCRIPTION:
# We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?
# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"
def number_to_string(num):
    return str(num)
print(number_to_string(25))
print(number_to_string(-125))

# Task5
# DESCRIPTION:
# You need to write a function that reverses the words in a given string. A word can also fit an empty string. 
# If this is not clear enough, here are some examples:
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
# Example (Input --> Output)
# "Hello World" --> "World Hello"
# "Hi There." --> "There. Hi"
def reverse(st):
    # st = list(st.split())
    # lst1 = []
    # for i in range(len(st))[::-1]:
    #     lst1.append(st[i])
    # st = " ".join(lst1)
    st = " ".join(list(reversed(st.split())))
    return st
print(reverse("Hello world!"))

# Task 6 
# DESCRIPTION:
# In this kata you will create a function that takes in a list and returns a list with the reverse order.
# Examples (Input -> Output)
# * [1, 2, 3, 4]  -> [4, 3, 2, 1]
# * [9, 2, 0, 7]  -> [7, 0, 2, 9]
def reverse_list(l):
    return list(reversed(l))
print(reverse_list([1, 2, 3, 4]))
print(reverse_list([9, 2, 0, 7]))

# Task 7
# DESCRIPTION:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
# Additionally, if the number is negative, return 0 (for languages that do have them).
# Note: If the number is a multiple of both 3 and 5, only count it once.
def solution(number):  
    sum = 0
    if number <= 0:
        return 0 
    num_set = [i for i in range(1, number) if i%3 == 0 or i%5 == 0]
    for y in range(len(num_set)):
        sum = sum + int(num_set[y])
    return sum 
print(solution(10))    

# Task 8 
# DESCRIPTION:
# You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel 
# is running out and the nearest pump is 50 miles away! You know that on average, your car runs  about 25 miles per gallon. 
# There are 2 gallons left.
# Considering these factors, write a function that tells you if it is possible to get to the pump or not.
# Function should return true if it is possible and false if not.
def zero_fuel(distance_to_pump, mpg, fuel_left):
    # if distance_to_pump / mpg <= fuel_left :
    #     return True
    # else:
    #     return False
    return True if distance_to_pump / mpg <= fuel_left else False
print(zero_fuel(50, 25, 2))
print(zero_fuel(67, 15, 4))

# Task 9
# DESCRIPTION:
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
# The function takes a name as its only argument, and returns one of the following strings:
# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.
def are_you_playing_banjo(name):
    # if name[0] == "R" or name[0] == "r":
    #     return str(name) + " plays banjo"
    # else:
    #     return str(name) + " does not play banjo"
    return str(name) + " plays banjo" if name[0] == "R" or name[0] == "r" else str(name) + " does not play banjo"
print(are_you_playing_banjo("Rocco")) 
print(are_you_playing_banjo("Ann")) 

# Task 10
# DESCRIPTION:
# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
def bool_to_word(boolean):
    return "Yes" if boolean == True else "No"
print(bool_to_word(True))
print(bool_to_word(False))

# Task 11
# Consider an array/list of sheep where some sheep may be missing from their place. 
# We need a function that counts the number of sheep present in the array (true means present).
# For example,
# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.
# Hint: Don't forget to check for bad values like null/undefined
def count_sheeps(sheep):
    # # count = 0
    # # for i in range(len(sheep)):
    # #     if bool(sheep[i]) == True:
    # #         count += 1
    # count = len([i for i in range(len(sheep)) if bool(sheep[i]) == True ])
    count = sheep.count(True)
    return count
print(count_sheeps([True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]))

# Task 12
# Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals 
# do not have the right tails. To help her, you must correct the broken function to make sure that 
# the second argument (tail), is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
# If the tail is right return true, else return false.
# The arguments will always be non empty strings, and normal letters.
def correct_tail(body, tail):
    return True if body[-1] == tail else False
print(correct_tail("Snake","e"))
print(correct_tail("Mouse","f"))