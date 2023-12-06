"""
Quick and dirty script to plot data from a csv file
"""

# Imports
import pandas as pd
from matplotlib import pyplot as plt
from IPython import embed

# Read the file
in_file = "clean_data/python_programming_language_5y_websearch.csv"
df_all = pd.read_csv(in_file)
df_all["Date"] = pd.to_datetime(df_all["Date"])
df_all = df_all[df_all.Year >= 2019]

# Plot all data, one single line
fig = plt.figure(figsize=(10, 6))

# Remove right and top borders from graph
ax = plt.subplot(111)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Plot
plt.plot(df_all["Date"], df_all["Python_Chile"], color="blue", alpha=0.75)
plt.xlabel("Año")
plt.ylabel("Índice de Google Trends")
plt.ylim(0, 100)
plt.savefig("images/python_chile_5y_2000.png", dpi=300, bbox_inches='tight')
plt.close()

# Plot one year at the time
# Only the last year has color
def year_plot(df, fig_filename, add_clases=False):
    fig = plt.figure(figsize=(10, 6))

    # Remove right and top borders from graph
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Years
    years = list(df.Year.unique())

    # Add light gray box to highlight beging and end of classes
    if add_clases:
        clases_start = int(pd.to_datetime("2023-03-06").strftime("%W"))
        clases_end = int(pd.to_datetime("2023-07-14").strftime("%W"))
        print(clases_start, clases_end)
        plt.axvspan(clases_start, clases_end, color="lightgray", alpha=0.25)
        clases_start = int(pd.to_datetime("2023-08-09").strftime("%W"))
        clases_end = int(pd.to_datetime("2023-12-16").strftime("%W"))
        print(clases_start, clases_end)
        plt.axvspan(clases_start, clases_end, color="lightgray", alpha=0.25)

    # Plot
    for i, y in enumerate(years):
        m = df.Year == y
        df_year = df.loc[m, :]
        color, alpha = "gray", 0.5 - 0.1*len(years) + 0.1*(i+1)
        if y == years[-1]:
            color, alpha = "blue", 0.75
        plt.plot(df_year["Weeknumber"], df_year["Python_Chile"], color=color, alpha=alpha)
        # Add text
        plt.text(df_year["Weeknumber"].iloc[-1], df_year["Python_Chile"].iloc[-1], y, fontsize=12, color=color, alpha=alpha)
    # Labels
    plt.xlabel("semana del año")
    plt.ylabel("Índice de Google Trends (Chile)")
    plt.ylim(0, 100)
    plt.savefig(fig_filename, dpi=300, bbox_inches='tight')

for y in range(2019, 2024):
    df_y = df_all[df_all.Year <= y]
    year_plot(df_y, f"images/python_chile_5y_{y}.png")

year_plot(df_y, f"images/python_chile_5y_{y}_clases.png", add_clases=True)
