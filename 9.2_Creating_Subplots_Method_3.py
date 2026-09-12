import matplotlib.pyplot as plt
import numpy as np  

print("\n")
print("Method 3:-Creating a Grid of Subplots")
print("\n")


fig, axes = plt.subplots(2, 2, figsize=(8, 6))  # Create 2×2 subplot grid

x = np.linspace(0, 5, 50)        # Generate values from 0 to 5

axes[0, 0].plot(x, np.sin(x))   # Sine plot
axes[0, 0].set_title("Sine")    # Set title

axes[0, 1].plot(x, np.cos(x), color="orange")  # Cosine plot
axes[0, 1].set_title("Cosine")

axes[1, 0].plot(x, x**2, color="green")        # Quadratic plot
axes[1, 0].set_title("Quadratic")

axes[1, 1].plot(x, np.log(x + 1), color="red") # Logarithmic plot
axes[1, 1].set_title("Log Function")

plt.tight_layout()               # Adjust spacing
plt.show()                       # Display all plots
