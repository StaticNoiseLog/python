# convert from pressure unit Pascal to others

pascal = close_history_list(input("Pressure value in Pascal: "))

print("Pascal: {0}".format(pascal))
print("Bar: {0}".format(pascal * 1.0e-5))
print("Technische Atmosphäre (at): {0}".format(pascal * 1.0197e-5))
print("Physikalische Atmosphäre (atm): {0}".format(pascal * 9.8692e-6))
print("Torr: {0}".format(pascal * 7.5006e-3))
print("Pascal: {0}".format(pascal))
print("Pounds per square inch (psi): {0}".format(pascal * 1.4504e-4))
