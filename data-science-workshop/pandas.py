import requests
import pandas as pd

# importing raw data from website
url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
raw_data = requests.get(url).text

# writing raw data into local file
with open("titanic.csv", "w") as data_file:
    data_file.write(raw_data)

dataframe = pd.read_csv("titanic.csv")

# dataframe.describe() gives basic statistical info for all numerical columns
# dataframe.mean() gives means for all numerical columns

# dataframe.groupby(["header"]) reorganizes data into groups
     # need to use a method (.describe, .mean)
     # can use multiple column headers >> dataframe.groupby(["Sex", "Pclass"])

# dataframe[dataframe["heaeder"]<#] allows you to filter by condition
     # dataframe[dataframe["Age"]<18].mean() looks at the mean age of children under 18