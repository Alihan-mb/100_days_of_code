import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

# temp_list = data["temp"].to_list()
#
# '''3 methods to find the average'''
# total = 0
# for temp in temp_list:
#     total += temp
#
# print(f"The average is {round(total/len(temp_list), 2) }")
#
# total = sum(temp_list)
# average = total / len(temp_list)
# print(f"The average is {round(average, 2)}")
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
#
# # Get data in columns
# print(data["condition"])
# print(data.condition)
#
# # data in the rows
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print((monday.temp * 9/5) + 32)
#
# monday_temp = monday.temp[0]
# print((monday_temp * 9/5) + 32)
# #
# # create a dataframe from scratch
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("new_data.csv")
#
# new_csv_file = pandas.read_csv("new_data.csv")
#
# # print(new_csv_file[new_csv_file.students == "James"])
#
# print(new_csv_file[new_csv_file.scores == new_csv_file.scores.max()])
# print(new_csv_file["James" == new_csv_file.students])

















