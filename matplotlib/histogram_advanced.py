"""Schreiben Sie ein Programm, das ein Histogramm der Sinus-Funktion y(t)=sin(t) er-
stellt. Hierzu sollen die Funktionswerte von t zwischen 0 und 63 mit einer Schrittweite
von 0.01 berechnet werden. Interpretieren Sie das Ergebnis und markieren Sie die
Maximalwerte der Sinusfunktion im Histogramm.
"""
import matplotlib.pyplot as plt
import numpy as npy

t = npy.arange(0, 63, 0.01)
sinuswerte = npy.sin(t)
plt.hist(sinuswerte, bins=20, color="yellow", linewidth=2)
plt.title('Histogramm einer Sinusfunktion')
plt.annotate("Maximalwerte", xy=(0.95, 905),
             xytext=(0, 920), arrowprops={"facecolor": "b"})
plt.show()
