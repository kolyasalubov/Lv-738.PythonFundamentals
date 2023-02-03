# Write a function that calculate thr number of characters included in given string.
# input: "hello"
# output: {"h":1,"e":1,"l":2,"o":1}

def calc_char(word):
    result = {}
    for i in range(len(word)):
        result.update({word[i]:word.count(word[i])})
    return result

print(calc_char("ababagalamaga"))