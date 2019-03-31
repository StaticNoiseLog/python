import numpy as np

x = np.arange(1, 6, 1)
y = np.arange(2, 12, 2)

print(x)
print(y)

print(x + y)
print(x - y)
print(x * y)
print(x ** y)

# dot product (Matrizenprodukt)
m1 = np.array([[1, 2], [0, 1]])
m2 = np.array([[1, 0], [1, 2]])
print(m1, "\ndot product\n", m2, "\nequals:\n", np.dot(m1, m2))

# inner product of two vectors
v1 = np.array([1, 2, 3])
v2 = np.array([1, 4, -5])
print('inner vector product: ', np.inner(v1, v2))


# boolean vector array as result from comparison
mixed_bag = np.array([14, 3, 7, 12, 4, 5, 6])
even_values = (mixed_bag % 2 == 0)
print(even_values)
