import matplotlib.pyplot as mpl
import numpy as np
x = np.linspace(-2, 2, 401)
mpl.plot((-2, 2), (0, 0), 'k')
mpl.plot(x, x**3, 'r')
mpl.gca().set_aspect(0.25)
mpl.show()
