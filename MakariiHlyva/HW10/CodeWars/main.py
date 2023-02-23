####################### Regular Ball Super Ball #############################

# class Ball(object):
#     def __init__(self, ball_type = 'regular'):
#         self.ball_type = ball_type

# ball1 = Ball()
# ball2 = Ball("super")

# print(ball1.ball_type)
# print(ball2.ball_type)

####################### Color Ghost #########################################


# from random import choice

# class Ghost(object):
#     def __init__(self):
#         self.color = choice(["white", "yellow", "purple", "red"])

# ghost = Ghost()
# print(ghost.color)



#################### Basic subclasses - Adam and Eve ########################

# def God():
#   return [Man(), Woman()]

# class Human:
#   def __init__(self):
#     pass

# class Man(Human):
#   def __init__(self):
#     pass

# class Woman(Human):
#   def __init__(self):
#     pass
    
    
# list = God()
# if isinstance(list[0], Man):
#   print("YES")


########################### Classy Classes ################################


# class Person:
#     def __init__(self, name, age):
#         self.name = str(name)
#         self.age = int(age)

#     def getinfo(self):
#         return f"{self.name}s age is {self.age}"
    

# class Person:
#     def __init__(self, name, age):
#         self.info = f"{name}s age is {age}"


############################ Building Spheres ##############################


# from math import pi

# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = float(radius)
#         self.mass = float(mass)
#         self.volume = 4 / 3 * pi * self.radius ** 3
#         self.area = 4 * pi * self.radius ** 2
#         self.density = self.mass / self.volume

#     def get_radius(self):                                               # radius of the Sphere (do not round it)
#         return self.radius
    
#     def get_mass(self):                                                 # mass of the Sphere (do not round it)
#         return self.mass
    
#     def get_volume(self):                                               # volume of the Sphere (rounded to 5 place after the decimal)
#         return round(self.volume, 5)     

#     def get_surface_area(self):                                         # surface area of the Sphere (rounded to 5 place after the decimal)
#         return round(self.area, 5)
    
#     def get_density(self):                                              # density of the Sphere (rounded to 5 place after the decimal)
#         return round(self.density, 5)
    
# ball = Sphere(2,50)
# print(ball.get_radius())
# print(ball.get_mass())
# print(ball.get_volume())
# print(ball.get_surface_area())
# print(ball.get_density())
        

############################### Python's Dynamic Classes #1 #########################


#------------ for codewars code script

# from re import match

# def class_name_changer(cls, new_name):
#         if match(r"^[A-Z]{1}[a-zA-Z0-9]{1,}$", new_name):
#             cls.__name__ = new_name
#         else:
#             raise Error


#------------ to check code local script

# from re import match

# def class_name_changer(cls, new_name):
#     try:
#         if match(r"^[A-Z]{1}[a-zA-Z0-9]{1,}$", new_name):
#             cls.__name__ = new_name
#         else:
#             raise ValueError(f"{new_name} is invalid name")
#     except ValueError as error:
#         print(error)

    # class MyClass:
    #     pass

    # myObject = MyClass();
    # print(MyClass.__name__, "MyClass")

    # class_name_changer(MyClass, "UsefulClass");
    # print(MyClass.__name__, "UsefulClass")

    # class_name_changer(MyClass, "SecondUsefulClass");
    # print(MyClass.__name__, "SecondUsefulClass")

    # class_name_changer(MyClass, "SecondUsefulCl____ass");
    # print(MyClass.__name__, "SecondUsefulClass")
