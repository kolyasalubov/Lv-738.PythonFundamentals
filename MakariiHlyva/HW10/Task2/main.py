#------------Some program with classes------------#


from re import match

class Human:
    def __init__(self, name):
        self.name = name

    def greetingMessage(self):
        print(f"Hello {self.name}, how are you today?")

    @staticmethod
    def some_method():
        print("Static method called")


class method(Human):
    def __init__(self, name):
        super().__init__(name)

    def isHomosapience(self):
        print(f"{self.name} is a Homosapience")

def check_name(name):                                                                               # function to check name is correct before make class with this name
    if match(r"^[A-Z]{1}[a-z]{2,}$", name):
        return True
    else:
        return False


def input_menu():                                                                                           
    
    while True:
        try:
            name = input("Please, enter your name, first letter have to be in upper case: ")
            if len(name) > 15:
                raise ValueError("Too long name")                                                   # if len(name) more than 15
            else:
                if check_name(name):                                                                # if name is real name :)
                    human = method(name)
                    human.greetingMessage()
                    human.some_method()
                    human.isHomosapience()
                else:
                    raise ValueError("You have entered not letteres")
            break
        except ValueError as error:
            print(error)


input_menu()