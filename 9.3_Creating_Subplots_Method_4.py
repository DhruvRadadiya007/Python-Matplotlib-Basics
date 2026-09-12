import matplotlib.pyplot as plt
import numpy as np  

print("\n")
print("Method 4:- Sharing Axes Across Subplots")
print("\n")


fig, axes = plt.subplots(2, 1, sharex=True, figsize=(8, 6))  # Create 2 plots with shared x-axis

x = np.linspace(0, 10, 100)       # Generate values from 0 to 10

axes[0].plot(x, np.sin(x))        # Plot sine wave
axes[0].set_title("Sine Wave")    # Set title

axes[1].plot(x, np.cos(x), color="purple")  # Plot cosine wave
axes[1].set_title("Cosine Wave")  # Set title

plt.show()                        # Display the figure
