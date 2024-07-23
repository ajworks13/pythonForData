import pandas as pd
import matplotlib.pyplot as plt

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
print("------------")
print(df.max())
print("------------")
print(df.head())


customers = pd.read_csv("data/customers-100.csv",
                        index_col=0, parse_dates=True)


print(customers.head())
customers.plot()

plt.show()
