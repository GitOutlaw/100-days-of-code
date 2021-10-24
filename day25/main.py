# with open("day25/weather_data.csv", encoding="utf8") as data_file:
#     data = data_file.read().split()
#     print(data)

import csv

with open("day25/weather_data.csv", encoding="utf8") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)


import pandas