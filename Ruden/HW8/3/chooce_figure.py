from functions_area import * 

def choice_figure():
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