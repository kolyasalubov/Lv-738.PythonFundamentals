def calculate_area_rectangle(width_rectangle, length_rectangle):
    return width_rectangle*length_rectangle

def calculate_area_triangle(base_tringle, height_tringle):
    return 0.5 * base_tringle * height_tringle

def calculate_area_circle(radius):
    return 3.14 * (radius ** 2)


print('Select the menu item to calculate the area:')
print('1. rectangle')
print('2. triangle')
print('3. circle')

menu = int(input('Enter menu number!: '))
if menu == 1:
        width_rectangle = float(input('Enter the width of the rectangle: '))
        length_rectangle = float(input('Enter the length of the rectangle: '))
        print(calculate_area_rectangle(width_rectangle, length_rectangle))
    
elif menu == 2:
        base_tringle = float(input('Enter the base of the triangle: '))
        height_tringle = float(input('Enter the height of the triangle: '))
        print(calculate_area_triangle(base_tringle, height_tringle))
    
elif menu == 3:
        radius = float(input('Enter the radius of the circle: '))
        print(calculate_area_circle(radius))
else:
        print('Error! Select menu from 1 to 3') 