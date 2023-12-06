"""
df = 
            Date C/C++   Java JavaScript Python     R
0    Jul 1, 2004   10%  30.2%       8.6%   2.5%  0.4%
1    Aug 1, 2004  9.7%  29.8%       8.7%   2.6%  0.4%
2    Sep 1, 2004  9.6%  29.6%       8.7%   2.7%  0.4%
...
"""

# Imports
import pandas as pd

# Get the correct table
html_file = "data/PYPL_29_worldwide.html"
table = pd.read_html(html_file)
df = table[1]

# Convert first column from weird string to datetime, to yyyy-mm-dd string
df["Date"] = pd.to_datetime(df["Date"])
df["Date"] = df["Date"].apply(lambda x: str(x.strftime("%Y-%m-%d")))
languages = list(df.columns[1:])

# Convert to percetanges, without the %. Some come as in "3.2%" and others as in "0.032"
# So convert depending on the case
for col in df.columns[1:]:
    try:
        df[col] = df[col].str.replace('%', '').astype(float)
    except:
        df[col] = df[col].apply(lambda x: 100*float(x))

# Get year, mm, dd
df["Year"] = df["Date"].apply(lambda x: int(x.split("-")[0]))
df["Month"] = df["Date"].apply(lambda x: int(x.split("-")[1]))
df["Day"] = df["Date"].apply(lambda x: int(x.split("-")[2]))

# Sort the columns
out_df = df[["Date", "Year", "Month", "Day"] + languages]

# Save as excel and csv
out_file = html_file.replace("data","clean_data")
out_df.to_excel(out_file.replace("html","xlsx"), index=False)
out_df.to_csv(out_file.replace("html","csv"), index=False)
print(out_df.head())