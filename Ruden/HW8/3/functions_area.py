from math import pi, pow


def calculate_area_rectangle(width_rectangle, length_rectangle):
    return width_rectangle*length_rectangle


def calculate_area_triangle(base_tringle, height_tringle):
    return 0.5 * base_tringle * height_tringle


def calculate_area_circle(radius):
    return pi * pow(radius,2)
