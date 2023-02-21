import math

def area_rectangle():
    '''Calculates the area of a rectangle'''
    side1=float(input('Enter the first side '))
    side2=float(input('Enter the second side '))
    area = side1*side2
    message = print(f'The area is {area}')
    return message

def area_triangle():
    '''Calculates the area of a triangle'''
    base=float(input('Please enter the base '))
    height=float(input('Please enter the height '))
    area = 0.5*base*height
    message = print(f'The area is {area}')
    return message

def area_circle():
    '''Calculates the area of a circle'''
    r=float(input('Please enter the radius '))
    area = math.pi*math.pow(r, 2)
    message = print(f'The area is {area}')
    return message



