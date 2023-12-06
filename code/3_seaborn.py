"""
Plot the dataset using seaborn
"""

# Import libraries
import pandas as pd
from matplotlib import pyplot as plt

# Read the data
df = pd.read_excel('data/dataset.xlsx')

# Plot
import seaborn as sns
sns.scatterplot(x = "x", y = "y", 
                data=df, hue="group",
                palette=['red','blue']).\
            set(title='Python Chile según Seaborn',
                xlabel='eje x', 
                ylabel='eje y')

# Save and show
plt.savefig('images/3_seaborn.png')