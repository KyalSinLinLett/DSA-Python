# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
weather_dict = {}

with open('./datasets/nyc_weather.csv', 'r') as f:
    for row in f:
        token = row.split(",")
        date = token[0]
        if date == 'date':
            continue
        weather_dict[date] = int(token[1])

#     What was the temperature on Jan 9?
print("Jan 9:", weather_dict['Jan 9'])

#     What was the temperature on Jan 4?
print("Jan 4:", weather_dict['Jan 4'])
