
class Human:

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f"Welcome {self.name}!")

    @classmethod
    def species(cls):
        return "Homosapiens"

    @staticmethod
    def home_message():
        return "Home - Earth"


person1 = Human("Josh")

person1.welcome_message()
print(Human.species())
print(Human.home_message())
print(person1.home_message())