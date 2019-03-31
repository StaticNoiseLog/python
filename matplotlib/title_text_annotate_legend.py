import numpy as npy
import matplotlib.pyplot as plt

t = npy.arange(0.0, 6.4, 0.1)
y = 5*npy.sin(t)
plt.plot(t, y, "ro-", linewidth=3, label="Sinus")
plt.title("Sinus-Funktion")
plt.text(1.5, 5.2, "Maximum")
plt.text(4.5, -5.5, "Minimum")
plt.annotate("Nulldurchgang", xy=(3.2, 0),
             xytext=(5, 3.5), arrowprops={"facecolor": "b"})
plt.legend() # show all labels in legend
#plt.legend(("Sinus", "otherLabel")) # specific labels only

plt.show()
