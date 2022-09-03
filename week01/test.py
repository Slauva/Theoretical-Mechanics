import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("WebAgg")  # Need to be installed tkinter

x = np.linspace(-5, 5, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()
