## Jenny's secret message

def greet(name):
    if name != "Johnny":
        return f"Hello, {name}!"
    else:
        return "Hello, my love!"
    
## Given two ordered pairs calculate the distance between them. Round to two decimal places. This should be easy to do in 0(1) timing.

def distance(x1, y1, x2, y2):
    return round((((x1 - x2)**2 + (y1 - y2)**2)**0.5), 2)

## Write a function taking in a string like WOW this is REALLY amazing
# and returning Wow this is really amazing. String should be capitalized and properly spaced.
# Using re and string is not allowed.

def filter_words(st):
    result = ""
    for char in st:
        if char  == " " and (len(result) == 0 or result[-1] == " "):
            continue
        elif char  == " " and result[-1] != " ":
            result += char
        elif len(result) == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

# We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?
# Examples (input --> output):

def number_to_string(num):
    return str(num)

# You need to write a function that reverses the words in a given string. A word can also fit an empty string.
# If this is not clear enough, here are some examples:
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

def reverse(st):
    list = st.split()
    list.reverse()
    return ' '.join(list)

# In this kata you will create a function that takes in a list and returns a list with the reverse order.

def reverse_list(l):
    'return a list with the reverse order of l'
    l.reverse()
    return l


# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).
# Note: If the number is a multiple of both 3 and 5, only count it once.
# Courtesy of projecteuler.net (Problem 1)

def solution(number):
    sum = 0
    if number < 0:
        return 0
    for num in range(number):
        if num%3 == 0 or num%5 == 0:
            sum += num
    return sum

# You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
# Considering these factors, write a function that tells you if it is possible to get to the pump or not.
# Function should return true if it is possible and false if not.

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg*fuel_left

# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    
# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

def count_sheeps(sheep):
    return sheep.count(True)

# Is this my tail?

def correct_tail(body, tail):
    return tail == body[-1]