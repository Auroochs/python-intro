import matplotlib.pyplot as plt
import numpy as np

# --- 1) Wykres liniowy ---
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure()
plt.plot(x, y, label='sin(x)')
plt.title('Wykres liniowy: sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.savefig('line_plot.png')
plt.show()

# --- 2) Wykres punktowy (scatter) ---
np.random.seed(42)
x2 = np.random.rand(50)
y2 = np.random.rand(50)

plt.figure()
plt.scatter(x2, y2, marker='o')
plt.title('Wykres punktowy')
plt.xlabel('x2')
plt.ylabel('y2')
plt.savefig('scatter_plot.png')
plt.show()
