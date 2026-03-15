import pandas as pd

data = {
    "name": ["Rahul", "Aman", "Riya"],
    "age": [25, 30, 22],
    "city": ["Delhi", "Mumbai", "Jaipur"]
}

df = pd.DataFrame(data)

# CSV New Column Add
df["salary"] = [50000, 60000, 45000]

df.to_csv("output.csv", index=False)

print("\n*************** Filter Data *************************\n")
print(df[df["age"] > 25])

print("\n*************** Sorting *************************\n")
print(df.sort_values(by="age"))


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
