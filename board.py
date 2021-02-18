from turtle import Turtle
import time

FONT=('Arial', 25, 'normal')

class Board(Turtle):
    def __init__(self):
        self.left = 0
        self.right = 0
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()

        self.score()

    def score(self):
        self.goto(0, -300)
        self.setheading(90)
        for i in range(0, 18):
            self.dot(7)
            self.fd(30)
        self.write(f"{self.left}    :    {self.right}", align="center", font=FONT)

    def increase_left(self):
        self.left += 1
        self.clear()
        self.score()

    def increase_right(self):
        self.right += 1
        self.clear()
        self.score()

    def winner(self, n):
        t = Turtle()
        t.color('white')
        t.penup()
        t.hideturtle()
        t.backward(60)
        t.write(f"Player {n} Win", font=FONT)
        time.sleep(1)
        t.clear()
        self.clear()
        self.score()