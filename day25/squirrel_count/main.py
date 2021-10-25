import pandas

data = pandas.read_csv("day25/squirrel_count/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirels_count, red_squirels_count, black_squirels_count]
} 
df = pandas.DataFrame(data_dict)
df.to_csv("day25/squirrel_count/squirrel_count.csv")


