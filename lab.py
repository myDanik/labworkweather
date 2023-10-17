import requests
from geopy.geocoders import *
import sys



def weather_json(city):
    if geolocator.geocode(city):
        true_city = geolocator.geocode(city)
        lat = float(true_city.latitude)
        lon = float(true_city.longitude)
    else:
        return sys.exit('Неверно указан город')
    params = {
        'lat': str(lat),
        'lon': str(lon),
        'appid': '2480c30e008a4930f0d6dd07a24b4545',
        'units': 'metric',
        'lang': 'ru'
    }
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?',params=params)
    if response:
        return response.json()
    else:
        return sys.exit('Error'+str(response.status_code))
geolocator = Nominatim(user_agent='Tester')
city = input('Введите название города с указанием региона\n')
true_city = geolocator.geocode(city)
print(true_city,'\nСейчас', str(weather_json(city).get('weather')[0].get('description')),',',weather_json(city).get('main').get('temp'),'°C, ощущается как',weather_json(city).get('main').get('feels_like'),'°C')