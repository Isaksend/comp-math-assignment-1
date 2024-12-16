import math
# Fourth equation
def f(x):
    return x**3 + x**2 + x + 7

def df(x):
    return 3*x**2 + 2*x + 1


# Second equation
# def f(x):
#     return x - math.cos(x)

# def df(x):
#     return 1 + math.sin(x)

# Sixth equation
# def f(x):
#     return math.cos(x) - x * math.exp(x)

# def df(x):
#     return -math.sin(x) - math.exp(x) * (1 + x)


def NewtonMethod(x0, tol, nmax):
    count = 0
    print(f"Initial guess: x0 = {x0}")
    while count < nmax:
        fx = f(x0)
        dfx = df(x0)
        # checking of dividing to  zero
        if dfx == 0:
            print("Derivative is zero. No solution found.")
            return
        
        h = fx / dfx
        x1 =x0 - h
        count += 1
        print(f"Iteration {count}: x = {x1:.3f}, h = {h:.3f}")
        
        if math.fabs(h)<tol:
            print(f"The root of the equation is x = {x1:.3f}")
            break
        x0 = x1
    print("Solution doesn't converge")

NewtonMethod(5, 0.001, 20)