def is_isogram(word):
    new_word = word.upper()
    for item in new_word:
        if new_word.count(item) > 1:
            return False
            break
    else:
        return True
        
st = (1,2,3)
newst = set(st)
print(newst)

