from tkinter import *
import os
from tkinter import CENTER
import pandas
import random

data = pandas.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")

# print(data_dict)
#
# random_number = random.randint(0, len(data_dict)-1)
# print(random_number)
# print(data_dict[random_number]["French"])
#
#
# a = data_dict[random_number]
# data_dict.remove(a)
# print(data_dict)

my_dict = dict()

for index, value in enumerate(data_dict):
    my_dict[index] = value

# a = pandas.DataFrame(my_dict)
# new_data = a.to_csv("words.csv", columns="French")
# print(new_data)










