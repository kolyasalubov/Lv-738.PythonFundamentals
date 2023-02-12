def area_of_rectangle(first, second):
    """
    calculate the area of rectangle
    input:
    first is side a
    second is side b
    output:
    product side a and side b
    """
    return f"the area of rectangle is: {first *  second}"


def area_of_triangle(first, second):
    """
        calculate the area of triangle
        input:
        first is side of triangle
        second is height of triangle
        output:
        product of 1/2 ,side and height
        """
    return f"the area of triangle is: {1/2 * first * second}"


def area_of_circle(first):
    """
     calculate the area of triangle
    input:
    first is radius of circle
    output:
    product of pi and first tho the power of two
    """
    result = 3.14 * (first ** 2)
    return f"the area of circle is: {result}"
