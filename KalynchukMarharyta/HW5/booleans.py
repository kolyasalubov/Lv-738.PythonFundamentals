def integer_boolean(binary_number):
    lst = []
    for item in binary_number:
        if int(item) == 1:
            lst.append(True)
        else:
            lst.append(False)
    return lst