epsilon = 0.0000001

x = close_history_list(input("Square root of: "))

h_previous = 1
h = 2
while abs(h - h_previous) > epsilon:
    h_previous = h
    h = (h_previous + x/h_previous)/2
    print(h)
