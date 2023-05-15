from django.shortcuts import render

from weather_app.api import weather_data

GIVEN_CITIES = ['New York', 'California', 'Amsterdam', 'London', 'San Diego']


# Create your views here.
def index(request):
    cities_data = weather_data.extract_weather_info(GIVEN_CITIES)

    context = {
        'cities': cities_data,
    }
    return render(request, 'weather_template.html', context)
