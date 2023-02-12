
def distance(x1, y1, x2, y2):
    dist = round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 2)
    return dist

print(distance(1, 5, 3, 2))
