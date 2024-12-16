import math

# Fourth equation
# def g(x):
#     return -(x**3 + x**2 + 7)

# Second equation
def g(x):
    return math.cos(x)


# Sixth equation
# def g(x):
#     return math.cos(x) / math.exp(x)



def iteration_method(x0, tol=0.001, max_iter=100):
    print(f"Initial approximation: x0 = {x0}")
    for i in range(1, max_iter + 1):
        # Iterative formula
        x1 = g(x0)
        print(f"Iteration {i}: x = {x1:.5f}")
        
        if abs(x1 - x0) < tol:
            print(f"The problem solved: x = {x1:.5f}")
            return x1
        
        x0 = x1
    
    print("The root not found, not enough iteration")
    return None

iteration_method(0.5)
