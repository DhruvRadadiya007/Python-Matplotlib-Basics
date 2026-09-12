import matplotlib.pyplot as plt
import numpy as np


x = np.random.rand(100)
y = np.random.rand(100)

colors = np.random.rand(100) # values for color mapping
sizes =200* np.random.rand(100) # random marker size    

plt.scatter(
            x,y,
            c=colors, # color based on values
            s=sizes, # marker size
            alpha=0.5,
            cmap='viridis' # color map
            )

plt.colorbar(label="color scale")
plt.title("Customized scatter plot")

plt.show()


