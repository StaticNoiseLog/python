import numpy as npy
import matplotlib.pyplot as plt

t = npy.arange(0.0, 6.4, 0.1)
y = 5*npy.sin(t)
z = 3*npy.cos(t)

plt.figure()

# subplot layout: 2 rows, 1 column; Sine plot is at position 1
plt.subplot(2, 1, 1, title="Sine")
plt.plot(t, y, color="red", linewidth=3)

# subplot layout: 2 rows, 1 column; Cosine plot is at position 2
plt.subplot(2, 1, 2, title="Cosine")
plt.plot(t, z, color="blue", linewidth=2)

plt.show()
