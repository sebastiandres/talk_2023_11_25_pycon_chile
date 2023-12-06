"""
Plot the dataset using matplotlib
"""

# Import libraries
import pandas as pd

# Read the data
df = pd.read_excel('data/dataset.xlsx')

# Plot using matplotlib
from matplotlib import pyplot as plt
plt.plot(df.x[df.group=="A"], df.y[df.group=="A"], ".r")
plt.plot(df.x[df.group=="B"], df.y[df.group=="B"], ".b")
plt.xlabel("eje x")
plt.ylabel("eje y")
plt.title("Python Chile según Matplotlib")
plt.axis('square')

# Show the plot
plt.savefig('images/1_matplotlib.png')
plt.show()