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

def secant_method(x0, x1, tol=0.001, max_iter=20):
    print(f"Initial approximation points: x0 = {x0}, x1 = {x1}")
    for n in range(1, max_iter + 1):
        if f(x1) - f(x0) == 0:
            print("Dividing to zero. Method can not be continue.")
            return None
        
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        print(f"Iteration {n}: x2 = {x2:.5f}, f(x2) = {f(x2):.5f}")
        
        if abs(x2 - x1) < tol:
            print(f"The root of equation: x = {x2:.5f}")
            return x2
        
        x0, x1 = x1, x2
    
    print("The root not found throw maximum number of iteration")
    return None


secant_method(0.5, 1.0)
