from turtle import *


def triangle(xa, ya, length):
    penup()
    goto(xa, ya)
    pendown()
    forward(length)
    left(120)
    forward(length)
    left(120)
    forward(length)
    left(120)
    reset()
    pensize(4)


triangle(-200, -300, 400)
triangle(-100, -200, 300)
triangle(0, 0, 200)
exitonclick()
