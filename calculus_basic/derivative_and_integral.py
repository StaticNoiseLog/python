def f(x):
    return x**2


def derivative(x):
    h = 1./1000.
    rise = f(x+h) - f(x)
    run = h
    slope = rise / run
    return slope


def integral(startingx, endingx, numberOfRectangles):
    width = (float(endingx) - float(startingx)) / numberOfRectangles
    runningSum = 0
    for i in range(numberOfRectangles):
        # each rectangle is 'width' after previous one
        height = f(startingx + i*width)
        area = height * width
        runningSum += area
    return runningSum


print(derivative(1))
print(derivative(2))
print(derivative(3))

print(integral(0, 1, 10000))
