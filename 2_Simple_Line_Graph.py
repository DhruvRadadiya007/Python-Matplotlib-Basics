import matplotlib.pyplot as plt
import numpy as np

print("\n")
print("Line PLot Graph")
print("\n")

x = np.arange(0,10) # values from 1 to 9
y = x**2 # squared values from x

plt.plot(x,y) # define x and y dataset and create line plot 
plt.title("Basic Line PLot") # plot title
plt.xlabel("X") # xlabel
plt.ylabel("X Squared") # y label

plt.grid(False) # grid 

plt.show() # display the plot

