"""
Quick and dirty script to plot data from a csv file
"""

# Imports
import pandas as pd
from matplotlib import pyplot as plt
from IPython import embed

# Read the file
in_file = "clean_data/PYPL_29_worldwide.csv"
df_all = pd.read_csv(in_file)

# Select the top 5 languages
N = 5
m = df_all["Date"] == "2023-11-01"
cols = list(df_all.columns[4:]) # Skip Date, Year, Month, Day
df_last_date = df_all.loc[m, cols]
df_last_date = df_last_date.T
df_last_date.columns = ["Last date"]
df_last_date.sort_values(by="Last date", inplace=True, ascending=False)
top_languages = list(df_last_date.index[0:N])
print(top_languages)

# Plot all years
def years_plot(df, fig_filename, add_covid=False):
    fig = plt.figure(figsize=(10, 6))
    # Remove right and top borders from graph
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    # Add light gray box to highlight beging and end of covid
    if add_covid:
        covid_start = pd.to_datetime("2020-03-11")
        covid_end = pd.to_datetime("2022-03-11")
        plt.axvspan(covid_start, covid_end, color="lightgray", alpha=0.25)
    # Plot
    for l in top_languages:
        # Regular values
        x_offset, y_offset, color = pd.DateOffset(days=30), -0.4, "gray"
        # Exceptions
        if l == "C/C++":
            y_offset += +0.5
        if l == "C#":
            y_offset += -0.5
        if l == "Python":
            color, alpha = "blue", 0.75
        # Plot
        plt.plot(df.index, df[l], label=l, color=color, alpha=alpha)
        # Add text next to last known value 
        plt.text(df.index[-1] + x_offset, df[l][-1] + y_offset, l, fontsize=12, color=color, alpha=alpha)
    # Labels
    plt.xlabel("Año")
    plt.ylabel("Índice PYPL")
    plt.ylim(0, 40)
    #plt.show()
    plt.savefig(fig_filename, dpi=300, bbox_inches='tight')


df = df_all[ ["Date", "Year"] + top_languages]
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)
years_plot(df, "images/top_5_from_2004.png", add_covid=False)
df_5y = df[df.Year >= 2017]
years_plot(df_5y, "images/top_5_from_2017_n_covid.png", add_covid=False)
years_plot(df_5y, "images/top_5_from_2017_y_covid.png", add_covid=True)

