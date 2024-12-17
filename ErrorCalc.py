import math
import matplotlib.pyplot as plt

def f(x):
    return x - math.cos(x)

def df(x):
    return 1 + math.sin(x)

def g(x):
    return math.cos(x)


real_root = 0.739085
tol = 0.001
max_iter = 20

x0, x1 = 0.5, 1.0
a, b = 0, 1

def absolute_error(real_root, approx_root):
    return abs(real_root - approx_root)

def relative_error(real_root, approx_root):
    return abs(real_root - approx_root) / abs(real_root) if real_root != 0 else 0

def BisectionMethod(a, b, real_root, tol=0.001, max_iter=20):
    approximations = []
    absolute_errors = []
    relative_errors = []
    for i in range(max_iter):
        c = (a + b) / 2
        approximations.append(c)
        abs_err = abs(real_root - c)
        rel_err = abs_err / abs(real_root)
        absolute_errors.append(abs_err)
        relative_errors.append(rel_err)

        if abs(f(c)) <= tol or abs(b - a) < tol:
            break
        elif f(a) * f(c) > 0:
            a = c
        else:
            b = c
    return absolute_errors, relative_errors


def NewtonMethod(x0, real_root, tol=0.001, max_iter=20):
    count = 0
    approximations = [x0]
    absolute_errors = [abs(real_root - x0)]
    relative_errors = [absolute_errors[0] / abs(real_root)]

    for _ in range(max_iter):
        x1 = x0 - f(x0) / df(x0)
        approximations.append(x1)
        abs_err = abs(real_root - x1)
        rel_err = abs_err / abs(real_root)
        absolute_errors.append(abs_err)
        relative_errors.append(rel_err)

        if abs(x1 - x0) < tol:
            break
        x0 = x1
    return absolute_errors, relative_errors


def SecantMethod(x0, x1, real_root, tol=0.001, max_iter=20):
    approximations = [x0, x1]
    absolute_errors = [abs(real_root - x0), abs(real_root - x1)]
    relative_errors = [absolute_errors[0] / abs(real_root), absolute_errors[1] / abs(real_root)]
    for _ in range(2, max_iter):
        if f(x1) - f(x0) == 0:
            print("Division by zero error. Stopping method.")
            break
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        approximations.append(x2)
        abs_err = abs(real_root - x2)
        rel_err = abs_err / abs(real_root)
        absolute_errors.append(abs_err)
        relative_errors.append(rel_err)
        if abs(x2 - x1) < tol:
            print(f"Converged to root: x = {x2:.6f}")
            break
        x0, x1 = x1, x2

    return absolute_errors, relative_errors


def IterationMethod(x0, real_root, tol=0.001, max_iter=20):
    approximations = [x0]
    absolute_errors = [abs(real_root - x0)]
    relative_errors = [absolute_errors[0] / abs(real_root)]

    for _ in range(max_iter):
        x1 = g(x0)
        approximations.append(x1)
        abs_err = abs(real_root - x1)
        rel_err = abs_err / abs(real_root)
        absolute_errors.append(abs_err)
        relative_errors.append(rel_err)
        if abs(x1 - x0) < tol:
            print(f"Converged to root: x = {x1:.6f}")
            break
        x0 = x1

    return absolute_errors, relative_errors

def plot_for_tolerance(tol1, tol2, real_root):
    methods = ["Bisection", "Newton-Raphson", "Secant", "Iteration"]
    results = {}

    for tol in [tol1, tol2]:
        results[tol] = {}
        results[tol]["Bisection"] = BisectionMethod(0, 1, real_root, tol)
        results[tol]["Newton-Raphson"] = NewtonMethod(0.5, real_root, tol)
        results[tol]["Secant"] = SecantMethod(0.5, 1.0, real_root, tol)
        results[tol]["Iteration"] = IterationMethod(0.5, real_root, tol)

    plt.figure(figsize=(12, 8))

    for i, tol in enumerate([tol1, tol2]):
        plt.subplot(2, 2, i + 1)
        for method in methods:
            abs_errors, _ = results[tol][method]
            plt.plot(abs_errors, label=f"{method} Method")
        plt.title(f"Absolute Error (Tolerance = {tol})")
        plt.xlabel("Iteration")
        plt.ylabel("Absolute Error")
        plt.legend()
        plt.grid()

        plt.subplot(2, 2, i + 3)
        for method in methods:
            _, rel_errors = results[tol][method]
            plt.plot(rel_errors, label=f"{method} Method")
        plt.title(f"Relative Error (Tolerance = {tol})")
        plt.xlabel("Iteration")
        plt.ylabel("Relative Error")
        plt.legend()
        plt.grid()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    real_root = 0.739085
    tolerance1 = 1e-2
    tolerance2 = 1e-6

    plot_for_tolerance(tolerance1, tolerance2, real_root)