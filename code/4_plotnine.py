"""
Plot the dataset using plotnine
"""

# Import libraries
import pandas as pd
from matplotlib import pyplot as plt

# Read the data
df = pd.read_excel('data/dataset.xlsx')

# Plot using plotnine
import plotnine as p9
my_plot = (
    p9.ggplot(df)
    + p9.aes(x='x', y='y')
    + p9.geom_point(data=df[df.group=="A"], color='red')
    + p9.geom_point(data=df[df.group=="B"], color='blue')
    + p9.labs(title='Python Chile según Plotnine',
              x='eje x', 
              y='eje y')
)


# Show the plot
#my_plot.save("scatterplot.png", width=10, height=10, dpi=300)
my_plot.draw(show=False).savefig('images/4_plotnine.png')
#plt.show()