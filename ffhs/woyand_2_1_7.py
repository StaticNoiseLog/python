from turtle import *
line = "M 270 113 L 135 113"
s, x1, y1, s, x2, y2 = line.split(" ")
x1 = int(x1)
y1 = int(y1)
print(x1, y1)
x2 = int(x2)
y2 = int(y2)
print(x2, y2)
print()
reset()
speed(0)
penup()
goto(x1, y1)
pendown()
goto(x2, y2)
exitonclick()
