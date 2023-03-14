def rectangle_area(width, height):
    return width * height

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return 3.14 * radius ** 2

def main():
    """
    This function prompts the user to select a shape and calculates its area using the corresponding function.
    """
    print("Select a shape to calculate its area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = int(input("Enter your choice (1, 2, or 3): "))

    if choice == 1:
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        area = rectangle_area(width, height)
        print("The area of the rectangle is:", area)
    elif choice == 2:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = triangle_area(base, height)
        print("The area of the triangle is:", area)
    elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        area = circle_area(radius)
        print("The area of the circle is:", area)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()
