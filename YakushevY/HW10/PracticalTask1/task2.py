class Human:

    def __init__(self,name):
        
        self.name = name
        

    def hello_human(self):
        print(f"Hello human, {self.name}")

    @staticmethod
    def some_message():
        print("hi")


class Kind(Human):
    def __init__(self):
        super().__init__("Anton")

    def what_kind(self):
        kind = str(input("What do you think you are Homsapiens?Yes/No: "))
        if kind=="Yes":
            print(f"Hello, {self.name} maby you are Homosapiens")
        else:
            print(f"Hello {self.name} you are Neanderthal")
       

a = Kind()
a.what_kind()
a.some_message()
a.hello_human()