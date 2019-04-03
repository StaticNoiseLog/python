import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(100, 200)

print(data)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(data)
ax.set_aspect('auto')

plt.show()