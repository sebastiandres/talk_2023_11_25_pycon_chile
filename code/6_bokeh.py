"""
Plot the dataset using bokeh
"""

# Import libraries
import pandas as pd
from matplotlib import pyplot as plt
from bokeh.io import export_png

# Read the data
df = pd.read_excel('data/dataset.xlsx')

# Plot using bokeh
import bokeh.plotting as bk
p = bk.figure(title="Python Chile según Bokeh", 
            x_axis_label="eje x", 
            y_axis_label="eje y")
m_A = df.group=="A"
p.circle(df.x[m_A], df.y[m_A], color="red")
m_B = df.group=="B"
p.circle(df.x[m_B], df.y[m_B], color="blue")

# Show the plot
#bk.show(p)
export_png(p, filename="images/6_bokeh.png")