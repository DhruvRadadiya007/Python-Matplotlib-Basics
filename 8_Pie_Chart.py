import matplotlib.pyplot as plt
import numpy as np

quantity = [50,30,20]
labels = ['apple','banana','cherry']


plt.pie(quantity,
        labels=labels,
        autopct="%1.1f%%",
        startangle=120
)

plt.title(" fruit distribution ")
plt.axis("equal")

plt.show()

