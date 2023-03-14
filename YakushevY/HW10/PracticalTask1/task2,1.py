


class Human:

    def __init__(self):
        name = input("Enter your name: ")
        self.name = name
        

    def hello_human(self):
        print(f"Hello human, {self.name}")

    @classmethod
    def kind_of_human(cls):
        name = input("Enter your name again: ")
        kind = str(input("What do you think you are Homsapiens?Yes/No: "))
        if kind=="Yes":
            print(f"Hello, {name} maby you are Homosapiens")
        else:
            print(f"Hello {name} you are Neanderthal")



    @staticmethod
    def some_message():
        print("hi")

a = Human()
a.hello_human()
a.kind_of_human()