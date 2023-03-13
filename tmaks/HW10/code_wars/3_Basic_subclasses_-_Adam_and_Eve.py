
class Human:
    def __init__(self):
        self.human = "Human"
        self.sub_class = None


class Man(Human):
    def __init__(self):
        self.sub_class = "Man"


class Woman(Human):
    def __init__(self):
        self.sub_class = "Woman"


def God():
    man = Man()
    woman = Woman()
    return man, woman


print(God())