from math import pi


def rectangle(edge1,edge2):
    area = edge1*edge2
    return area


def triang(edge1,edge2,edge3):
    p =(edge1+edge2+edge3)/2
    area =(p*(p-edge1)*(p-edge2)*(p-edge3))**0.5
    return area


def rounde(radius):
    area = pi*(radius**2)
    return area
