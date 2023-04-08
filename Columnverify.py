import pandas as pd

# read data from file
data = pd.read_csv("country.csv")

# print number of rows and columns
print("Number of rows:", data.shape[0])
print("Number of columns:", data.shape[1])

# print column names
print("Column names:", data.columns)
