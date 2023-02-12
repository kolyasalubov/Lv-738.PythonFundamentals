# Task3. Write a function that calculates the number of characters
# included in a given string
# • input: "hello"
# • output: {"h":1, "e":1,"l":2,"o":1}

def numberOfChar(string):
    all_chars = {}
    for character in string:
        if character in all_chars:
            all_chars[character] += 1
        else:
            all_chars[character] = 1
    return print(all_chars)

numberOfChar('string')
        