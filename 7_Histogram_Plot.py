import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100)

plt.hist(data,bins=30,edgecolor = "black") # bins are the number of bars you want to show

plt.title(" Simple Bar Chart ")
plt.xlabel(" Category ")
plt.ylabel(" Value ")

plt.show()

