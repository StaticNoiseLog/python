from turtle import *
color("blue")  # Zeichenfarbe blau
pensize(60)  # Liniendicke 60 Pixel
left(90)  # Turtle vertikal stellen
forward(100)  # Vertikale Linie zeichnen
goto(0, 0)  # Zum Ursprung zurueck gehen
left(120)  # Die Schildkroete um 120 Grad nach links drehen
forward(100)  # Zweite Linie zeichnen
goto(0, 0)  # Wieder zum Ursprungspunkt zurueck gehen
left(120)  # Die Schildkroete weitere 120 Grad nach links drehen
forward(100)  # Dritte Linie zeichnen
print("Zum Beenden in die Grafik klicken!")
exitonclick()
