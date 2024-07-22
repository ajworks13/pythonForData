import pandas as pd

df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["A", "B", "C"])

print(df)
print("------------")
print(df.columns)
print("------------")
print(df.info())
print("------------")
print(df.describe())
print("------------")
print(df["A"].unique())
print("------------")
print(df.shape)
print("------------")
print(df.size)
