import matplotlib.pyplot as plt
import numpy as np

print("\n")
print("Customizing Line PLot")
print("\n")

x = np.linspace(0,10,50) # generate 50 values from 0 to 10
y = np.sin(x) # compute sin values

plt.plot(
         x,y,
         color='purple', # line color 
         linestyle = '--', # Dashed line style 
         linewidth = 2, # line thickness
         marker = "o", # marking the value points
         markersize = 6, # marker size
         label = "sin(x)" # legend label shows in the right corner of the plot
         )

plt.title("Customized Line PLot") # plot title
plt.xlabel("X") # xlabel
plt.ylabel("sin(x)") # y label

plt.legend() # show legend

plt.grid(True) # grid 

plt.show() # display the plot
