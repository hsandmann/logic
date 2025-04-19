import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
matplotlib.use("module://matplotlib_pyodide.html5_canvas_backend")

eq = lambda x: x**3 - 8*x**2 + 16*x

x = np.linspace(-2, 7)
plt.axhline(0, color='lightcoral') # x = 0
plt.axvline(0, color='lightcoral') # y = 0

fig, ax = plt.subplots()
fig.tight_layout()

plt.show()