import matplotlib.pyplot as plt
import  numpy as np

Categories = ['A','B','C','D']
Values = [10,20,30,40]

plt.bar(Categories,Values)
plt.title(" Simple Bar Chart ")
plt.xlabel(" Category ")
plt.ylabel(" Value ")

plt.show()