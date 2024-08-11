import pandas as pd
import matplotlib.pyplot as plt

# df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["A", "B", "C"])


# print(df)
# print("------------")
# print(df.columns)
# print("------------")
# print(df.info())
# print("------------")
# print(df.describe())
# print("------------")
# print(df["A"].unique())
# print("------------")
# print(df.shape)
# print("------------")
# print(df.size)
# print("------------")
# print(df.max())
# print("------------")
# print(df.head())


# customers = pd.read_csv("data/customers-100.csv",
#                         index_col=0, parse_dates=True)


# print(customers.head())
# customers.plot()

# plt.show()


data = pd.DataFrame({"Yes": [50, 21], "No": [131, 2]})
data2 = pd.DataFrame(
    {'Bob': ['I liked it.', 'It was awful.'],
        'Sue': ['Pretty good.', 'Bland.']},
    index=['Product A', 'Product B'])

'''

Series

A Series, by contrast, is a sequence of data values. If a DataFrame is a table, a Series is a list. And in fact you can create one with nothing more than a list

'''
se = pd.Series([1, 2, 3, 4, 5])

se2 = pd.Series([30, 35, 40], index=['2015 Sales',
                '2016 Sales', '2017 Sales'], name='Product A')

customers = pd.read_csv("data/customers-100.csv")


print(se2)
