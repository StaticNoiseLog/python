# %%
msg = "Hello World"
print(msg)

# %%
msg = "Hello again"
print(msg)

# %%
n = 6
step = 3 / (n - 1)
x = 0
for i in range(n):
    print('i: ', i)
    print('x: ', x)
    x += step
