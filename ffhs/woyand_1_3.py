# Aufgabe 1.3 Woyand

while True:
    x = input("integer x: ")
    x = close_history_list(x)
    if x <= 0:
        break
    y = 0.5*x**3 - 0.5*x**2 + 2*x + 5
    print("x: {0}, y: {1}".format(x, y))

print("bye...")
