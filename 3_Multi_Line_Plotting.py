import matplotlib.pyplot as plt
import numpy as np

print("\n")
print("Multi-Line PLot")
print("\n")

x = np.linspace(0,10,200) # generate 50 values from 0 to 10

plt.plot(x, np.sin(x), label ='sin(x)')
plt.plot(x, np.cos(x), label ='sin(x)')
plt.plot(x, np.tan(x), label ='sin(x)',alpha=0.5) # alpha = transparency

plt.title("Multiple Trigonometric functions") # plot title
plt.xlabel("X") # xlabel
plt.ylabel("Y") # y label
plt.ylim(-2,2) # set a limited value range

plt.legend() # show legend

plt.grid(True) # grid 

plt.show() # display the plot

