# with open ("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))

# average = sum(temp_list)/len(temp_list)
# print(average)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)



# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])
# >>       day  temp condition
# >>   6  Sunday    24     Sunny


# monday = data[data.day == "Monday"]
# print(monday.condition)
# 0    Sunny
# Name: condition, dtype: object

# 월요일의 기온을 섭씨에서 화씨로 변경해보기
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp + 9/5 + 32
# print(monday_temp_F)

#
# # Create a dataframe from scratch
# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }
#
# data= pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color = data["Primary Fur Color"]

# gray = sum(data["Primary Fur Color"] == "Gray")
# cinnamon = sum(data["Primary Fur Color"] == "Cinnamon")
# black = sum(data["Primary Fur Color"] == "Black")
# print(gray)

#SOLUTION
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
#
#
# data_dict = {
#     "Fur Color" : ["Gray","Cinnamon","Black"],
#     "Count" : [grey_squirrels_count,cinnamon_squirrels_count,black_squirrels_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count")

print(data[data["Primary Fur Color"] == "Gray"])