# Aufgabe 1.9 Woyand
import turtle

turtle.reset()
turtle.speed(0)

forward_dist = 20
forward_dist_increment = 5

number_of_turns = int(turtle.textinput("How many turns?", "Number of turns:"))

while number_of_turns > 0:
    turtle.fd(forward_dist)
    turtle.lt(90)
    number_of_turns = number_of_turns - 1
    forward_dist = forward_dist + forward_dist_increment
    print("new length: ", forward_dist)

turtle.textinput("Pause", "Hit OK!")
print("bye...")
