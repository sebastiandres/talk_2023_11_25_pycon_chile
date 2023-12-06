def get_weeknumber(yyyymmdd):
    """
    Returns the weeknumber of a given date.
    yyyymmdd is a string with the date in the format "yyyy-mm-dd".
    """
    yyyy, mm, dd = yyyymmdd.split("-")
    my_date = datetime.date(int(yyyy), int(mm), int(dd))
    wn = my_date.strftime("%W")
    return wn

# Imports
import pandas as pd
import datetime

# Read the file
in_file = "data/python_programming_language_5y_websearch.csv"
df = pd.read_csv(in_file, skiprows=1)


# Rename Week to Date, because it's so confusing
df.rename(columns={"Week": "Date"}, inplace=True)

# Add columns
df["Year"] = df["Date"].apply(lambda x: x.split("-")[0])
df["Month"] = df["Date"].apply(lambda x: x.split("-")[1])
df["Day"] = df["Date"].apply(lambda x: x.split("-")[2])
df["Weeknumber"] = df["Date"].apply(get_weeknumber)

# Rename columns 
df.rename(columns={"Python: (Chile)": "Python_Chile"}, inplace=True)

# Save
out_df = df[["Date", "Year", "Month", "Day", "Weeknumber", "Python_Chile"]]
out_file = "clean_data/python_programming_language_5y_websearch.csv"
out_df.to_csv(out_file, index=False)
out_df.to_excel(out_file.replace(".csv", ".xlsx"), index=False)