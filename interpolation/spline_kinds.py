import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x_axis = np.r_[0:10:11j]
y = np.sin(x_axis)

xnew = np.r_[0:10:100j]

plt.plot(x_axis, y, linewidth=1.0)

for kind in ['nearest', 'zero', 'slinear', 'linear', 'quadratic', 'cubic']:
    f = interpolate.interp1d(x_axis, y, kind=kind)
    ynew = f(xnew)
    plt.plot(xnew, ynew, label=kind)

plt.show()