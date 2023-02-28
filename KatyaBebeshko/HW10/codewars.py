## ball super ball

class Ball():
    
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type

## color ghost

import random

class Ghost():

    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

## adam eve

class Human():
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(), Woman()]

## classy classes

class Person:

    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"

## building spheres


import math

class Sphere():
    
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
	
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return round(4/3 * math.pi * math.pow(self.radius, 3), 5)
    
    def get_surface_area(self):
        return round(4 * math.pi * math.pow(self.radius, 2), 5) 
    
    def get_density(self):
        return round(self.mass/self.get_volume(), 5)
    

## dynamic classes

import re

class MyClass():
    pass

def class_name_changer(self, nameNew):
    if re.search(r"[A-Z]", nameNew[0]) and re.search(r"[a-z],[0-9]", nameNew):
        self.__name__ = nameNew
        return True
    else:
        return False
    



