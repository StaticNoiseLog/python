import matplotlib.pyplot as plt
import numpy as np

theta = np.arange(0, 2*np.pi, .01)[1:]

plt.polar(theta, abs(np.sin(theta)))
plt.polar(theta, abs(np.cos(theta)))
plt.show()
