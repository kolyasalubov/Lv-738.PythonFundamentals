# Task 2.
# Create a class Human, everyone has a name, create a method in the class that displays a welcome message to each person.
# Create a class method in the class that returns information that it is a species of "Homosapiens".
# And in the class create a static method that returns an arbitraty message.

class Human:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        result = print(f"Hello {self.name}.")
        return result

    def species(self):
        return "Homosapiens"
    
    @staticmethod
    def message():
        result = print("You live on planet Earth.")
        return result


person_1 = Human("Bob")
person_1.greeting()
print("You are " + person_1.species())
person_1.message()