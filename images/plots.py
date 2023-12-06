import pandas as pd
import matplotlib.pyplot as plt
import datetime

def get_weeknumber(yyyymmdd):
    """
    Returns the weeknumber of a given date.
    yyyymmdd is a string with the date in the format "yyyy-mm-dd".
    """
    yyyy, mm, dd = yyyymmdd.split("-")
    my_date = datetime.date(int(yyyy), int(mm), int(dd))
    wn = my_date.strftime("%W")
    return wn

fpath = "PYPL_popularity_index.csv"
df = pd.read_csv(fpath)
df["Year"] = df["Date"].apply(lambda x: int(x.split("-")[0]))
df["Other languages"] = 100 - df["Python"] - df["Java"] - df["JavaScript"] - df["C/C++"] - df["R"]
x_cols = 'Date'
y_cols = ['C/C++', 'Java', 'JavaScript', 'Python', 'R', 'Other languages']
# Plot
ax = df.plot(x=x_cols, y=y_cols, figsize=(10, 6), grid=True)
# Save
plt.savefig('PYPL_popularity_index_allyears.png')
plt.close()
# Plot last 5 years
df = df[df["Year"] >= 2017]
ax = df.plot(x=x_cols, y=y_cols, figsize=(10, 6), grid=True)
plt.savefig('PYPL_popularity_index_5years.png')
plt.close()


# File structure
# Month,Python: (Chile)
# 2004-01,6
fpath = "python_programming_language_5y_websearch.csv"
df = pd.read_csv(fpath, skiprows=1)
ax = df.plot(x='Week', y='Python: (Chile)', figsize=(10, 6), grid=True)
plt.savefig('python_programming_language_5y_websearch.png')
plt.close()

# Plot by year
fpath = "python_programming_language_5y_websearch.csv"
df = pd.read_csv(fpath, skiprows=1)
df["Year"] = df["Week"].apply(lambda x: x.split("-")[0])
df["Weeknumber"] = df["Week"].apply(get_weeknumber)
df.sort_values(by="Weeknumber", inplace=True)
#from IPython import embed; embed()

plt.figure(figsize=(10, 6))
for year in df["Year"].unique():
    df_year = df[df["Year"] == year]
    x = df_year["Weeknumber"]
    y = df_year["Python: (Chile)"]
    ax = plt.plot(x, y, label=year)
plt.savefig('python_programming_language_5y_websearch2.png')
plt.close()

# File structure
# Month,Python: (Chile)
# 2004-01,6
fpath = "python_programming_language_5y_youtube.csv"
df = pd.read_csv(fpath, skiprows=1)
print(df.head())
ax = df.plot(x='Month', y='Python: (Chile)', figsize=(10, 6), grid=True)
plt.savefig('python_programming_language_5y_youtube.png')
plt.close()
