from turtle import Screen
from racket import Racket
from board import Board
from ball import Ball
import time
import random

LEFT_END = -580
RIGHT_END = 580

screen = Screen()
screen.setup(width=1200,height=600)
screen.bgcolor('black')
screen.title("Naru's Ping-Pong Game")
screen.tracer(0)

board = Board()
ball = Ball()

player_left = Racket()
player_right = Racket()
player_left.make_rackets(LEFT_END)
player_right.make_rackets(RIGHT_END)

screen.listen()
screen.onkey(player_left.up, "w")
screen.onkey(player_left.down, "s")
screen.onkey(player_right.up,"Up")
screen.onkey(player_right.down,"Down")


while True:
    screen.update()
    time.sleep(0.08)

    ball.move()

    for i in player_left.rackets:
        if i.distance(ball) < 20:
            angle = random.randint(-10,10)
            ball.turn(angle)

    for i in player_right.rackets:
        if i.distance(ball) < 20:
            angle = random.randint(-10, 10)
            ball.turn(angle)

    if ball.xcor() > 600 or ball.xcor() < -600 or ball.ycor() > 300 or ball.ycor() < -300:
        if ball.xcor() > 0:
            board.winner('Left')
            board.increase_left()

        else:
            board.winner('Right')
            board.increase_right()


        ball.reset()

