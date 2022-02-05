import pandas

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].max()
monday = data[data.day == "Monday"]

max_temp_day = data[data["temp"] == data["temp"].max()]

monday_temp_fahrenheit = (monday["temp"] * 1.8) + 32
print(monday_temp_fahrenheit)

#create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Ramona"],
    "scores": [76, 86, 90]
}

student_data = pandas.DataFrame(data_dict)

student_data.to_csv("new_data.csv")