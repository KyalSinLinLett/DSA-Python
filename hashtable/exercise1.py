# nyc_weather.csv contains new york city weather for first few days in the month of January.
# Write a program that can answer following,

weather_dict = {}

with open('./datasets/nyc_weather.csv', 'r') as f:
    for row in f:
        token = row.split(",")
        date = token[0]
        if date == 'date':
            continue
        weather_dict[date] = int(token[1])

# What was the average temperature in first week of Jan

total = 0
lim = 7
i = 1
for _, temp in weather_dict.items():
    total += temp
    if i == lim:
        break
    i += 1

average = int(total / lim)

print("Average temp =", average)

# What was the maximum temperature in first 10 days of Jan

max = 0
for _, temp in weather_dict.items():
    if temp > max:
        max = temp

print("The max temp is:", max)
