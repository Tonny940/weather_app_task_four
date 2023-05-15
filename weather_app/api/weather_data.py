from weather_app.api import api

cities = ['New York', 'California', 'Amsterdam', 'London', 'San Diego']


def extract_weather_info(weather):
    city_weather_info = []
    for city in cities:
        data = api.get_weather_data(city)
        city_weather_info.append(data)

    return city_weather_info


def min_average_temp(data_info):
    coldest_city = min(data_info, key=lambda city: data_info[city]["temp"])
    average_temp = sum([data_info[city]["temp"] for city in data_info]) / len(data_info)
    message = f"Coldest city is {coldest_city}: {data_info[coldest_city]['temp']}°C\n" \
              f"Avg temperature: {int(average_temp)}°C"
