# when upper and lower case counting separately
def count_char_in_word(word):
    res = {}
    for char in word:
        if char in res:
            continue
        else:
            res.update({str(char): word.count(char)})
    return res


print(count_char_in_word("helLowWorld"))


# when upper and lower case counting together
def count_char_in_word(word):
    res = {}
    new_word = word.lower()
    for char in new_word:
        if char in res:
            continue
        else:
            res.update({str(char): new_word.count(char)})
    return res


print(count_char_in_word("helLowWorld"))
