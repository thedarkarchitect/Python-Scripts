from tkinter import colorchooser
import pandas as pd

data = pd.read_csv("squirrel_census\Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = data["Primary Fur Color"].to_list()
gray_color = 0
red_color = 0
black_color = 0

for m in colors:
    if m == "Cinnamon":
        red_color += 1
    elif m == "Gray":
        gray_color += 1
    elif m == "Black":
        black_color += 1

data_dict ={
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray_color, red_color, black_color]
}

#makes the dataframe 
new_data = pd.DataFrame(data_dict)

# another way
# grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])