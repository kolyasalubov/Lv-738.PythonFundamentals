from math import pi


class Sphere:

    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(4 / 3 * pi * self.radius ** 3, 5)

    def get_surface_area(self):
        return round(4 * pi * self.radius ** 2, 5)

    def get_density(self):
        return round(self.mass / (4 / 3 * pi * self.radius ** 3), 5)


new_sphere = Sphere(5, 15)
new_sphere.get_volume()
new_sphere.get_surface_area()
new_sphere.get_density()
