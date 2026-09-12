import matplotlib.pyplot as plt
import numpy as np     


print("\n")
print("Method 1:- Using subplot functions")
print("\n")

x = np.linspace(1,10,100)


plt.figure(figsize=(10, 4))       # Create figure with custom size

# First subplot
plt.subplot(1, 2, 1)              # 1 row, 2 columns, plot 1
plt.plot(x, np.sin(x))            # Plot sine wave
plt.title("Sine Wave")            # Set title

# Second subplot
plt.subplot(1, 2, 2)              # 1 row, 2 columns, plot 2
plt.plot(x, np.cos(x), color="red")  # Plot cosine wave
plt.title("Cosine Wave")          # Set title

plt.tight_layout()                # Adjust spacing between subplots
plt.show()                        # Display the figure


print("\n")
print("Method 2:-  Creating Grid of Subplots")
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
plt.show()  