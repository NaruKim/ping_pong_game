import turtle

class Racket():
    def __init__(self):
        self.rackets = []

    def make_rackets(self, n):
        for i in range(4):
            t = turtle.Turtle('square')
            t.color('white')
            t.penup()
            t.hideturtle()
            t.goto(n, i*20)
            t.showturtle()
            self.rackets.append(t)

    #아래로 갈때는 rackets[0]을 움직이고, 위로 갈때는 rackets[3]을 움직인다.
    def up(self):
        for i in self.rackets:
            i.setheading(90)
            i.fd(20)

    def down(self):
        for i in self.rackets:
            i.setheading(270)
            i.fd(20)