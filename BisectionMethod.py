import math
a = -2
b = 0
tol = 0.01
count = 0
nmax = 1

def CalcFormula(x):
    return math.exp(x) - x ** 2

def BisectionMethod(a, b, nmax):
    global count
    while count <= nmax:
        c = (a + b) / 2
        if abs(CalcFormula(c)) <= tol:
            print(str(c) + " is the root")
            break
        elif CalcFormula(a) * CalcFormula(c) > 0:
            a = c
        else:
            b = c
        count += 1
        if count > nmax:
            print("Maximum iterations reached. Approximate root: " + str(c))
    print("The root: " + str(c) + ", f(c): " + str(CalcFormula(c)))

BisectionMethod(a, b, 7)
