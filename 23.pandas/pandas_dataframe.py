"""
    Pandas is a Python library used for working with data sets.
    It has functions for analyzing, cleaning, exploring, and manipulating data.
    The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis"

    Pandas allows us to analyze big data and make conclusions based on statistical theories.
    Pandas can clean messy data sets, and make them readable and relevant.
    Relevant data is very important in data science.
"""

import matplotlib.pyplot as plt
import pandas as pd

mydataset = {"cars": ["BMW", "Volvo", "Ford"], "passings:": [3, 7, 2]}

myvar = pd.DataFrame(mydataset)
print(myvar)
print(pd.__version__)


################################################################
# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.
################################################################

a = [1, 7, 2]
myvar = pd.Series(a)
print(f"print 1 dimensional array: {myvar}")


# the values are labeled with their index number. First value
# has index 0, second value has index 1 etc.
print(f"label: {myvar[0]}")

# create our own labels
myvar = pd.Series(a, index=["x", "y", "z"])
print(f"created our labels: \n{myvar}")


# Key/Value Object as Series, The keys of the dictionary become the labels.
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(f"key/value pair as series: \n{myvar}")

# create a series using only data from day1 and day2
myvar = pd.Series(calories, index=["day1", "day2"])
print(f"create a series using only data from day1 and day2: \n{myvar}")


################################################################
# DataFrames is a Data sets in Pandas are usually multi-dimensional tables.
# Series is like a column, a DataFrame is the whole table.
################################################################
data = {"calories": [420, 380, 390], "duration": [50, 40, 50]}

myvar = pd.DataFrame(data)
print(f"Dataframe: \n{myvar}")

# use loc attribute to Locate Row
print(f"locate row: return row 0: \n{myvar.loc[0]}")
print(f"locate row: return row 0 and row 1: \n{myvar.loc[[0,1]]}")

# Named Indexes - create your own index on DataFrame
myvar = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(f"Dataframe with custom index: \n{myvar}")
print(f"locate row with custom index day2: \n{myvar.loc['day2']}")

################################################################
# Load a comma separated file (CSV file) into a DataFrame
################################################################
df = pd.read_csv(
    "c:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\23.pandas\\data.csv"
)

# use to_string() to print the entire DataFrame.
# without using to_string(), for large DataFrame
# with many rows, Pandas will only return the first
# 5 rows, and the last 5 rows
print(f"load CSV file into DataFrame: \n{df.to_string()}")

# check system's maximum rows
print(f"check system's maximum rows: {pd.options.display.max_rows}")

# change the max number of row to display the entire DataFrame
pd.options.display.max_rows = 999

################################################################
# Load json file into a DataFrame
################################################################
df = pd.read_json(
    "c:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\23.pandas\\data.json"
)
print(f"load json file into DataFrame: \n{df}")

# JSON objects have the same format as Python dictionaries.
# load python dictionary into DataFrame

data = {
    "Duration": {"0": 60, "1": 60, "2": 60, "3": 45, "4": 45, "5": 60},
    "Pulse": {"0": 110, "1": 117, "2": 103, "3": 109, "4": 117, "5": 102},
    "Maxpulse": {"0": 130, "1": 145, "2": 135, "3": 175, "4": 148, "5": 127},
    "Calories": {"0": 409, "1": 479, "2": 340, "3": 282, "4": 406, "5": 300},
}

df = pd.DataFrame(data)
print(f"Load Python Dictionary into DataFrame: \n{df}")

################################################################
# Viewing the Data
################################################################
# The head() method returns the headers and a specified number
# of rows, starting from the top. Default 5 rows will be returned
print(f"return first 10 rows of the DataFrame: \n{df.head(10)}")

# tail() method for viewing the last rows of the DataFrame.
print(f"return last 5 rows of the DataFrame: \n{df.tail()}")

# info(), that gives you more information about the data set.
print(f"information about the data set \n{df.info()}")

################################################################
# Cleaning the Data
################################################################
df = pd.read_csv(
    "C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\23.pandas\\data_cleaning.csv"
)

# remove rows that contain empty cell
# By default, the dropna() method returns a new DataFrame, and will not change the original.
new_df = df.dropna()
print(f"remove rows that contain empty cell: \n{new_df.to_string()}")

# use the inplace = True argument to change the original DataFrame
# df.dropna(inplace=True)
# print(f"remove rows that contain empty cell in original DataFrame: \n{df.to_string()}")

# fillna() method allows us to replace empty cells with a value
# df.fillna(130, inplace=True)
# print(f"replace empty cells with a value 130: \n{df.to_string()}")

# calculate the mean (average value),
# median (the value in the middle, after you have sorted all values ascending)
# or mode (the value that appears most frequently)
# value of the column to replace empty cells
x = df["Calories"].mean()
# x = df["Calories"].median()
# x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace=True)
print(f"replace empty cells with a mean calculation: \n{df.to_string()}")


# Convert all cells in the 'Date column into dates
df["Date"] = pd.to_datetime(df["Date"], format="mixed", errors="coerce")
print(f"Convert all cells in the 'Date column into dates: \n{df.to_string()}")

# Remove rows with a NULL value in the "Date" column
df.dropna(subset=["Date"], inplace=True)
print(f"Remove rows with a NULL value in the 'Date' column: \n{df.to_string()}")

# fix wrong value by replacing a new value
# set "Duration" = 45 in row 7
df.loc[7, "Duration"] = 45
print(f"set 'Duration' = 45 in row 7: \n{df.to_string()}")

# Loop through all values in the "Duration" column.
# If the value is higher than 120, set it to 120
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120

print(f"If the value is higher than 120, set it to 120: \n{df.to_string()}")

# Delete rows where "Duration" is higher than 120:
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)

print(f"Delete rows where 'Duration' is higher than 120: \n{df.to_string()}")

# discover duplicate
print(f"duplicate value exists: \n{df.duplicated()}")

# drop_duplicates() method to remove duplicate rows
df.drop_duplicates(inplace=True)
print(f"dropped duplicate rows: \n{df.to_string()}")

################################################################
# Data Correlations
################################################################
# corr() method calculates the relationship between each column
# it ignores "not numeric" columns.
# The number varies from -1 to 1.

# 1 means that there is a 1 to 1 relationship (a perfect correlation),
# and for this data set, each time a value went up in the first column,
# the other one went up as well.

# 0.9 is also a good relationship, and if you increase one value,
# the other will probably increase as well.

# -0.9 would be just as good relationship as 0.9, but if you increase
# one value, the other will probably go down.

# 0.2 means NOT a good relationship, meaning that if one value goes
# up does not mean that the other will.

print(f"relationship between each column: \n{df.corr()}")

################################################################
# Plotting
# Pyplot, a submodule of the Matplotlib library to visualize
# the diagram on the screen
################################################################
df = pd.read_csv(
    "C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\23.pandas\\data.csv"
)
# plot() method to create diagrams.
df.plot()
plt.show()

# Scatter Plot
# Use scatter plot with the kind argument
df.plot(kind="scatter", x="Duration", y="Calories")
plt.show()

# Histogram
# A histogram needs only one column.
# shows us the frequency of each interval,
# e.g. how many workouts lasted between 50 and 60 minutes
df["Duration"].plot(kind="hist")
plt.show()
