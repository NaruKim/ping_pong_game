from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('white')
        self.speed(7)

    def move(self):
        self.fd(15)

    def turn(self, angle):
        self.setheading(180+angle+self.heading())

    def reset(self):
        self.goto(0,0)