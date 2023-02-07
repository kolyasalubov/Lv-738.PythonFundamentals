

def letter_count(word: str):

    letter_dict = {

    }

    for letter in set(word):
        letter_dict[letter] = word.count(letter)

    return letter_dict


#---------------------------------------------------------------------



print(letter_count("tree"))

