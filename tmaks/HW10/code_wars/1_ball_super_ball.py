
class Ball:
    def __init__(self, object=None):

        if object == None:
            self.ball_type = "regular"
        else:
            self.ball_type = object


ball1 = Ball()
ball2 = Ball("super")
print(ball1.ball_type)
print(ball2.ball_type)
