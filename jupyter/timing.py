# %%
def sum1(n):
    s = 0
    for k in range(1, n+1):
        s += k
    return s

%timeit sum1(10000)

# %%


def sum2(n):
    return n * (n+1) // 2


%timeit sum2(10000)