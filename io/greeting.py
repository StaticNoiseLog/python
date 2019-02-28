from math import pi

name = input("Your name: ")
print("hi " + name)

print("Pi in scientific notation: %e" % pi)

while True:
    your_number = float(input("Your lucky number: "))
    if your_number <= 0.0:
        print("You are lost.")
        print("Lost in negativity!")
    elif 0.0 < your_number <= 1.0:
        print("Well done!")
    elif 1.0 < your_number <= 2.0:
        print("ALMOST!")
    else:
        print("Gambling too high, my friend...")
