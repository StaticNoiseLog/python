import matplotlib.pyplot as plt
import numpy as npy
from scipy.interpolate import interp1d

t = npy.linspace(0.0, 2*npy.pi, 100)
support_points = npy.linspace(0.0, 2*npy.pi, 8)

sin_t = npy.sin(t)

print("support_points: ", support_points)

support_points_t = npy.sin(support_points)

plt.plot(t, sin_t, linewidth=1.0)

plt.scatter(support_points, support_points_t, c="k")

xnew = npy.linspace(0.0, 2*npy.pi, 100)

f = interp1d(support_points, support_points_t)
f2 = interp1d(support_points, support_points_t, kind='cubic')

print("f2: ", f2)
print("type(f2): ", type(f2))

#plt.plot(support_points, support_points_t, 'o', xnew, f2(xnew), '-')
plt.plot(support_points, support_points_t, 'o', t, f(t), '-', t, f2(t), '--')


# plt.plot(t, sin_t, linewidth=2)
# plt.plot(t, cos_t, "r", linewidth=2)
plt.xlabel('time in seconds')
plt.ylabel('y(t)')
plt.title('sine replicated with splines')
plt.grid(True)
plt.show()