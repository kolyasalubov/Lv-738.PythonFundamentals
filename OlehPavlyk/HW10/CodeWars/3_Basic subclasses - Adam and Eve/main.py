class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def god():
    return [Man(), Woman()]


print(god())
