
# Create a function that takes a string, 
# checks if it has the same number of "x"s and "o"s and returns either True or False.
'''
Return a boolean value (True or False).
Return True if the amount of x's and o's are the same.
Return False if they aren't the same amount.
The string can contain any character.
When "x" and "o" are not in the string, return True.
'''

def X_O(word):
    x_count, o_count = 0, 0
    
    for i in word:
        if i == 'x' or i == 'X':
            x_count += 1
            
        elif i == 'o' or i == 'O':
            o_count += 1
            
    if x_count == o_count:
            word = True
    else: word = False
    
    return word