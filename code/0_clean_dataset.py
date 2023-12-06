import pandas as pd
df = pd.read_excel('data/dataset_original.xlsx')
df['y'] = - df['y']
df.x = (df.x - df.x.mean()) / df.x.abs().max()
df.y = (df.y - df.y.mean()) / df.y.abs().max()

# Get random 1000 from A and random 1000 from B
N = 2800
df_new = pd.concat([df.loc[df.group=="A", :].sample(n=N), 
                df.loc[df.group=="B", :].sample(n=N)])

# Order one row A and one row B, and so on
new_index = []
for i in range(0, N):
    new_index += [i, i+N]
df_new = df_new.iloc[new_index, :].reset_index(drop=True)
print(df_new.head())

# Some stats
print(df_new.describe(include='all').fillna(""))

# Save the new dataset
df_new.to_excel('data/dataset.xlsx', index=False)

# Plot the df
df = df_new
from matplotlib import pyplot as plt
plt.plot(df.x[df.group=="A"], df.y[df.group=="A"], ".b")
plt.plot(df.x[df.group=="B"], df.y[df.group=="B"], ".r")
plt.show()