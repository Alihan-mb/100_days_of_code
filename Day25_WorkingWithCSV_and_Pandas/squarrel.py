# import pandas
#
# data = pandas.read_csv("squirrels.csv")
#
# gray_count = data["Primary Fur Color"].value_counts()["Gray"]
# cinnamon_count = data["Primary Fur Color"].value_counts()["Cinnamon"]
# black = data["Primary Fur Color"].value_counts()["Black"]
#
# squirrel_data = {
#     "Fur color": ["Grey", "Cinnamon", "Black"],
#     "Count": [gray_count, cinnamon_count, black]
# }
#
# squirrel = pandas.DataFrame(squirrel_data)
# squirrel.to_csv("squirrel_csv.csv")
#
# squirrel_csv = pandas.read_csv("squirrel_csv.csv")
# print(squirrel_csv)
import pandas as pd

data = pd.read_csv("squirrels.csv")
colors = data["Primary Fur Color"].value_counts()

df = pd.DataFrame(colors)
csv = df.to_csv("squirrel_count.csv")
b = pd.read_csv("squirrel_count.csv")
print(b)