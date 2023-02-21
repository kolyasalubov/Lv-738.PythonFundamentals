def correct_tail(body, tail):
    index = len(body)-len(tail)
    if body[index] == tail:
        return True
    else:
        return False
    

