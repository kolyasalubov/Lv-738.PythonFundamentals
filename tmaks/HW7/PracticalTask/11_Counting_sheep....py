
def count_sheeps(sheep):
    present = sheep.count(True)
    if present == len(sheep):
        return len(sheep)
    else:
        return present
