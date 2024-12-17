import math
import matplotlib.pyplot as plt
import pandas as pd

# The function is second equation
def f(x):
    return x - math.cos(x)

def df(x):
    return 1 + math.sin(x)

def g(x):
    return math.cos(x)

tol = 0.001
a, b = 0, 1       # Interval for Bisection method
x0 = 0.5          # Initial approximation
x1 = 1          # Second approximation for secant method
max_iter = 20

def BisectionMethod(a, b, nmax):
    count = 0
    if f(a) * f(b) >= 0:
        print("Bisection method fails: f(a) and f(b) must have opposite signs.")
        return []
    approximations = []
    while count <= nmax:
        c = (a + b) / 2
        approximations.append(c)
        if abs(f(c)) <= tol or abs(b - a) < tol:
            print(str(c) + " is the root")
            break
        elif f(a) * f(c) > 0:
            a = c
        else:
            b = c
        count += 1
    return approximations


# Newton-Raphson Method
def NewtonMethod(x0, tol, nmax):
    count = 0
    approximations = [x0]
    print(f"Initial guess: x0 = {x0}")
    while count < nmax:
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            print("Derivative is zero. No solution found.")
            return approximations
        h = fx / dfx
        x1 = x0 - h
        approximations.append(x1)
        count += 1
        print(f"Iteration {count}: x = {x1:.3f}, h = {h:.3f}")
        if math.fabs(h) < tol:
            print(f"The root of the equation is x = {x1:.3f}")
            break
        x0 = x1
    else:
        print("Solution doesn't converge")
    return approximations

def SecantMethod(x0, x1, tol=0.001, max_iter=20):
    approximations = [x0, x1]
    print("\nSecant Method:")
    for n in range(1, max_iter + 1):
        if f(x1) - f(x0) == 0:
            print("Dividing by zero. Method cannot continue.")
            return approximations
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        approximations.append(x2)
        print(f"Iteration {n}: x2 = {x2:.5f}, f(x2) = {f(x2):.5f}")
        if abs(x2 - x1) < tol:
            print(f"The root of the equation: x = {x2:.5f}")
            return approximations
        x0, x1 = x1, x2
    print("The root not found within the maximum number of iterations.")
    return approximations

# Iteration Method
def IterationMethod(x0, tol=0.001, max_iter=20):
    approximations = [x0]
    print("\nIteration Method:")
    for i in range(1, max_iter + 1):
        x1 = g(x0)
        approximations.append(x1)
        print(f"Iteration {i}: x = {x1:.5f}")
        if abs(x1 - x0) < tol:
            print(f"The problem solved: x = {x1:.5f}")
            break
        x0 = x1

    print("The root not found, not enough iterations.")
    return approximations


bisection_approximations = BisectionMethod(a, b, 20)
iteration_approximations = IterationMethod(x0)
newton_approximations = NewtonMethod(x0, tol,20)
secant_approximations = SecantMethod(x0, x1)


# Visualization part

plt.figure(figsize=(10, 6))
plt.plot(bisection_approximations, label="Bisection Method", marker='^')
plt.plot(iteration_approximations, label="Iteration Method", marker='o')
plt.plot(newton_approximations, label="Newton-Raphson Method", marker='x')
plt.plot(secant_approximations, label="Secant Method", marker='s')
plt.axhline(0.739085, color='r', linestyle='--', label="Exact Root ≈ 0.739")
plt.xlabel("Iteration")
plt.ylabel("Approximate Root Value")
plt.title("Comparison of Numerical Methods")
plt.legend()
plt.grid()
plt.show()

# Limitation number of iteration for correctly compare results
iterations = max(len(bisection_approximations),
                 len(iteration_approximations),
                 len(newton_approximations),
                 len(secant_approximations))

def pad_list(lst, length):
    return lst + ['...'] * (length - len(lst))

bisection_approximations = pad_list(bisection_approximations, iterations)
iteration_approximations = pad_list(iteration_approximations, iterations)
newton_approximations = pad_list(newton_approximations, iterations)
secant_approximations = pad_list(secant_approximations, iterations)

#This is data frame for table
data = {
    "Root": [f"x{i}" for i in range(iterations)],
    "1st method (Bisection)": bisection_approximations,
    "2nd method (Iteration)": iteration_approximations,
    "3rd method (Newton-Raphson)": newton_approximations,
    "4th method (Secant)": secant_approximations,
}

df = pd.DataFrame(data)
print(df)
df.to_excel("comparative_analysis.xlsx", index=False)