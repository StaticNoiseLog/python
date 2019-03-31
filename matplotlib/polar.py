"""Archimedean spiral:
r(φ) = 2*φ for 0 < φ <360°
"""
import matplotlib.pyplot as plt
import numpy as npy

theta = npy.arange(361)  # 0 .. 360
theta_radians = npy.radians(theta)  # convert angles to radians: 0 to 2*pi
r = 2*theta_radians
plt.polar(theta_radians, r)
plt.title('Archimedean spiral')
plt.show()
