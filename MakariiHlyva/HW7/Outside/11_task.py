#----------Counting sheep...---------#

def count_sheeps(sheep):
    counter = 0
    for index in range(0, len(sheep), 1):
        if sheep[index] == True:
            counter += 1

    return counter