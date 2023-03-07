from random import choice


class Ghost(object):
    def __init__(self):
        self.color = choice(["white", "yellow", "purple", "red"])

go = Ghost()
print(go.color)
