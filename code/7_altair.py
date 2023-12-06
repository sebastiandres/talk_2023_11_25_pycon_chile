"""
Plot the dataset using altair
"""

# Import libraries
import pandas as pd

# Read the data
df = pd.read_excel('data/dataset.xlsx')

# Plot using altair - order keyword was VERY important
import altair as alt
title = alt.TitleParams("Python Chile según Altair")
chart_1 = alt.Chart(df[df.group=="A"], title=title).\
            mark_circle().\
            encode(
                x=alt.X('x', title='eje x'), 
                y=alt.Y('y', title='eje y'),
                color=alt.value('red')
                ) 
chart_2 = alt.Chart(df[df.group=="B"]).\
            mark_circle().\
            encode(
                x=alt.X('x'), 
                y=alt.Y('y'),
                color=alt.value('blue')
                ) 
chart = chart_1 + chart_2

# Save and show
chart.save('images/7_altair.html')
#chart.show()