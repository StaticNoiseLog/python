# used oeis.org to fix bad example in Teschl p. 178
# Generate: 1/1 1/2 1/4 1/8 1/16 with different formula that gives
# same result only for first five members of the sequence (vs. )
def recfn(n, maxIterations):
    if n > maxIterations:
        return 1
    res = 1 / ((n**4 - 6*n**3 + 23*n**2 - 18*n + 24)/24)  # found with oeis.org
    # res = 1 - (262*n + 83*(n**2) - 14*(n**3) + (n**4))/384 # bad example in Teschl p. 178
    print("n: ", n, ", res: ", res)
    recfn(n + 1, maxIterations)


recfn(1, 10)
