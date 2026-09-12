import matplotlib.pyplot as plt  # import matplotlib for plotting
import numpy as np # import numpy for data 

print("\n")
print("Sample Plot for structure understanding")
print("\n")

x = np.linspace(1,10,100) # getting 100 equally spaced values from 0 to 9 
y = np.sin(x) # getting sin of each value created in x

plt.plot(x,y) # plot is used to plot the x axis and y axis
plt.title("Sin Wave") # adds title to the plot 
plt.xlabel("X-axis") # label the x axis with appropriate name
plt.ylabel("Y-axis") # label the y axis with appropriate name

plt.grid(True) # this is used to show or hide a grid in the plot

plt.show() # this is used to show the plot

print("\n")
print("Simple Line Graph Plot")
print("\n")