import pandas as pd

df = pd.read_csv("data.csv")

print("\n")
print(df)

print("\n")
print(df["name"])

print("\n")
print(df.head())

print("\n")
print(df.info())
print(df.describe())





# | Command      | Use            |
# | ------------ | -------------- |
# | `read_csv()` | CSV read       |
# | `head()`     | first rows     |
# | `tail()`     | last rows      |
# | `info()`     | dataset info   |
# | `describe()` | statistics     |
# | `drop()`     | column delete  |
# | `fillna()`   | missing values |
# | `groupby()`  | aggregation    |