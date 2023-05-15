import requests

api_key = "039a12d23806eea26ccefd5251862476"


def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    return {'city': city,
            'clouds': data['weather'][0]['description'],
            'temp': int(data['main']['temp']),
            'humidity': data['main']['humidity'],
            }
