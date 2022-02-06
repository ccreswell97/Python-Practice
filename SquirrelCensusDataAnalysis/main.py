from pandas import read_csv, DataFrame

def main():
    squirrel_data = read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    gray_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
    cinnamon_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
    black_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
    
    squirrel_dict = {
        "Fur Color": ["Gray", "Cinnamon", "Black"],
        "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
    }
    DataFrame(squirrel_dict).to_csv("squirrel_colors.csv")

if __name__ == "__main__":
    main()