"""
Plot the dataset using plotly
"""

# Import libraries
import pandas as pd
from matplotlib import pyplot as plt

# Read the data
df = pd.read_excel('data/dataset.xlsx')

# Plot
import plotly.express as px
fig = px.scatter(df, x="x", y="y", color='group',
                labels={"x": "eje x", "y": "eje y"},
                title="Python Chile según Plotly")
fig.update_yaxes(scaleanchor="x", scaleratio=1)

# Show the plot
fig.write_image("images/2_plotly.png")
plt.show()
