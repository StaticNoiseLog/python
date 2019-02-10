from turtle import *
reset()
pensize(1)
speed(0)

hilbert_seq = "a"

for _ in range(5):
    new_seq = ""
    for char in hilbert_seq:
        if char == "a":
            new_seq += "-bF+aFa+Fb-"
        elif char == "b":
            new_seq += "+aF-bFb-Fa+"
        else:
            new_seq += char
    hilbert_seq = new_seq

for char in hilbert_seq:
    if char == "F":
        forward(9)
    elif char == "+":
        right(90)
    elif char == "-":
        left(90)

x = 3 + 2j - (4 + 4j)

textinput("Pause", "Hit OK!")
