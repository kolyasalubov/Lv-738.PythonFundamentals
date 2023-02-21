# №1 Jenny's secret message
def greet(name):    
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


# №2 Simple: Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round(((x2-x1)**2 + (y2-y1)**2)**0.5, 2)


# №3 No yelling!
def filter_words(st):
    st = st.capitalize()
    return ' '.join(st.split())


# №4 Convert a Number to a String!
def number_to_string(num):
    return str(num)


# №5 Reversing Words in a String
def reverse(st):
    st = st.strip()
    words = st.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)


# №6 Reverse List Order
def reverse_list(l):
    return list(reversed(l))


# №7 Multiples of 3 or 5
def solution(number):
    sum = 0
    for number in range(1, number):
        if number % 3 == 0 or number % 5 == 0:
            sum += number
    return sum


# №8  Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if (distance_to_pump / (mpg * fuel_left)) <= 1 else False


# №9 Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


# №10 Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else: 
        return "No"


# №11 Counting sheep...
def count_sheeps(sheep):
    
    return sheep.count(True)

# №12 Is this my tail?
def correct_tail(body, tail):
    sub = body[-1]
    if sub == tail:
        return True
    else:
        return False

