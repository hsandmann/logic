import matplotlib.pyplot as plt
import numpy as np
from io import StringIO

eq = lambda x: x**3 - 8*x**2 + 16*x

x = np.linspace(-2, 7)
plt.axhline(0, color='lightcoral') # x = 0
plt.axvline(0, color='lightcoral') # y = 0

fig, ax = plt.subplots()
fig.tight_layout()

buffer = StringIO()
plt.savefig(buffer, format="svg")
print('aqui')
print(buffer.read())
print('la')
