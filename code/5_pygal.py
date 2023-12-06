"""
Plot the dataset using pygal
"""

# Import libraries
import pandas as pd
from matplotlib import pyplot as plt

# Read the data
df = pd.read_excel('data/dataset.xlsx')

# Plot using pygal
import pygal
xy_chart = pygal.XY()
data_A = df.loc[df.group=="A", ['x','y']].values
xy_chart.add('A', data_A, stroke=False, color='red')
data_B = df.loc[df.group=="B", ['x','y']].values
xy_chart.add('B', data_B, stroke=False, color='blue')
xy_chart.x_title = 'eje x'
xy_chart.y_title = 'eje y'
xy_chart.title = 'Python Chile según Pygal'

# Show the plot
xy_chart.render_to_png("images/5_pygal.png")

