def seq5(n, nResult, maxIterations):
    if n > maxIterations:
        return 1
    print("n: ", n, ", nResult: ", nResult)
    seq5(n + 1, (n + 1) * nResult, maxIterations)

seq5(1, 1, 8)
