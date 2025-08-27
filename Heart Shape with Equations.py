import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 1000)
y = np.linspace(-2, 2, 1000)
X, Y = np.meshgrid(x, y)
F = (X**2 + Y**2 - 1)**3 - X**2 * Y**3

plt.contour(X, Y, F, [0], colors="red")
plt.title("Heart Curve")
plt.show()
