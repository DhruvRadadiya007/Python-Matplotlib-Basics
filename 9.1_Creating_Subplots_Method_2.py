import matplotlib.pyplot as plt
import numpy as np  

print("\n")
print("Method 2:- Creating Subplots Using plt.subplots()")
print("\n")

fig, axes = plt.subplots(1, 2, figsize=(10, 4))  # Create figure with 2 subplots

x = np.linspace(0, 10, 100)       # Generate values from 0 to 10

axes[0].plot(x, np.sin(x), color='blue')   # Plot sine on first subplot
axes[0].set_title("Sine Function")          # Set title

axes[1].plot(x, np.cos(x), color='green')   # Plot cosine on second subplot
axes[1].set_title("Cosine Function")        # Set title

plt.show()                        # Display the figure
