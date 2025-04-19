# Import libraries
import matplotlib.pyplot as plt
import numpy as np
# from pyodide import display
import io
import PIL.Image
import base64

# Define a helper function to display the plot
def show_plot(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    img = PIL.Image.open(buf)
    img_str = 'data:image/png;base64,' + base64.b64encode(img.tobytes()).decode('UTF-8')
    print(img_str)

    print(img.tobytes())

# Create and display the plot
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
ax.plot(x, y)
ax.set_title("Sine Wave")
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")

# plt.show()

# Use the helper function instead of plt.show()
show_plot(fig)


# import matplotlib.pyplot as plt
# import numpy as np
# from io import StringIO
# from js import document
# import base64

# eq = lambda x: x**3 - 8*x**2 + 16*x

# x = np.linspace(-2, 7)
# plt.axhline(0, color='lightcoral') # x = 0
# plt.axvline(0, color='lightcoral') # y = 0

# fig, ax = plt.subplots()
# fig.tight_layout()

# buffer = StringIO()
# plt.savefig(buffer, format="svg")
# buffer.seek(0)
# print('aqui')
# print(buffer.getvalue())
# print('la')

# # img_str = 'data:image/svg;svg+xml;,' + buffer.getvalue()
# # print(img_str)
# # #Here I am setting the value of src of HTML element to that of the image string.
# # pfig = document.getElementById("pyplotfigure")
# # pfig.setAttribute("src",img_str)