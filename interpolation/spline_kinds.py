import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

support_points_x  = np.r_[0:10:11j]
support_points_y = np.sin(support_points_x )
plt.scatter(support_points_x, support_points_y, c="k", label="support points")

x = np.r_[0:10:100j]

plt.plot(support_points_x , support_points_y, linewidth=1.0)

for kind in ['nearest', 'zero', 'slinear', 'linear', 'quadratic', 'cubic']:
    f = interpolate.interp1d(support_points_x , support_points_y, kind=kind)
    ynew = f(x)
    plt.plot(x, ynew, label=kind)

plt.legend()
plt.show()