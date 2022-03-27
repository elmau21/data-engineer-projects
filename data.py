from matplotlib import pyplot as plt
import numpy as np

#100 random data along 3 dimensions 

x, y, scale = np.random.randn(3,100)
fig, ax = plt.subplots()

#Map each onto a scatter
ax.scatter(x=x, y=y, c=scale, s=np.abs(scale)*500)
ax.set(title="Some random data, created with JupyerLab!")
plt.show()