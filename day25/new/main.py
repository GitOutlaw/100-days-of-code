# with open("day25/weather_data.csv", encoding="utf8") as data_file:
#     data = data_file.read().split()
#     print(data)

# import csv

# with open("day25/weather_data.csv", encoding="utf8") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

data = pandas.read_csv("day25/weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# print(data["temp"].mean()) # average temp
# print(data["temp"].max()) # max temp

# Get Data in Columns
# print(data["condition"])
# print(data.condition) # object

# Get Data in Row
# print(data[data.day =="Monday"]) # Get data in row
# print(data[data.temp == data.temp.max()]) # Get max temp

# Converts monday temp into farenheit
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_tempF = monday_temp * 9/5 + 32
# print(monday_tempF)

# Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("day25/new_data.csv")

