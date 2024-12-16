import numpy as np
import matplotlib.pyplot as plt
# Define the function
def f(x):
 return x**2 - 25/16
# For f(x) = x^2 - 25/16, the zeros are x = ±5/4
zeros = np.array([5/4, -5/4])
# Generate x values for plotting
x_values = np.linspace(-2, 2, 400)
y_values = f(x_values)
# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label=r'$f(x) = x^2 - \frac{25}{16}$', color='blue')
plt.axhline(0, color='black', lw=0.5, ls='--') # x-axis
plt.axvline(0, color='black', lw=0.5, ls='--') # y-axis
# Mark the zeros on the graph
plt.scatter(zeros, f(zeros), color='red', zorder=5)
plt.text(5/4, 0.1, r'$\left(\frac{5}{4}, 0\right)$', fontsize=10, ha='center')
plt.text(-5/4, 0.1, r'$\left(-\frac{5}{4}, 0\right)$', fontsize=10, ha='center')
# Set labels and title
plt.title('Graph of $f(x) = x^2 - \\frac{25}{16}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.ylim(-1, 2)
plt.xlim(-2, 2)
plt.grid()
plt.legend()
plt.show()