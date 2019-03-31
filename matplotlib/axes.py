import numpy as npy
import matplotlib.pyplot as plt

t = npy.arange(0.0, 6.4, 0.1)
y = 5*npy.sin(t)
z = 3*npy.cos(t)
plt.plot(t, y, "ro-", linewidth=3)
plt.title("Sinus-Funktion")
plt.axes([0.6, 0.55, 0.25, 0.25])
plt.plot(t, z, "b+-", linewidth=2)
plt.title("Kosinus-Funktion")
plt.show()
