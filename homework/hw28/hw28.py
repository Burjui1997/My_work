import requests
from dataclasses import dataclass
from marshmallow import Schema, fields, validate, ValidationError
from marshmallow_jsonschema import JSONSchema
from marshmallow_dataclass import class_schema
import json


def get_weather(city_name):
    api_key = "23496c2a58b99648af590ee8a29c5348"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'lang': 'ru',
        'units': 'metric',
        'appid': api_key
    }
    response = requests.get(base_url, params=params)
    return response.json()


@dataclass
class CurrentWeather:
    city: str
    temperature: float
    description: str
    humidity: int
    wind_speed: float
    visibility: float


CurrentWeatherSCHEMA = class_schema(CurrentWeather)


class CurrentWeatherSchema(CurrentWeatherSCHEMA):
    city = fields.Str(required=True)
    temperature = fields.Float(required=True, validate=validate.Range(min=-100, max=100))
    description = fields.Str(required=True)
    humidity = fields.Int(required=True, validate=validate.Range(min=0, max=100))
    wind_speed = fields.Float(required=True, validate=validate.Range(min=0))
    visibility = fields.Float(required=True, validate=validate.Range(min=0))


json_schema = JSONSchema().dump(CurrentWeatherSchema())

with open('hw_weather.json', 'w', encoding='utf-8') as file:
    json.dump(json_schema, file, indent=4, ensure_ascii=False)

city = input("Введите название города: ")

weather_data = get_weather(city)

weather = CurrentWeather(
    city=weather_data['name'],
    temperature=weather_data['main']['temp'],
    description=weather_data['weather'][0]['description'],
    humidity=weather_data['main']['humidity'],
    wind_speed=weather_data['wind']['speed'],
    visibility=weather_data.get('visibility')
)

json_data = CurrentWeatherSchema().dump(weather)

try:
    data = CurrentWeatherSchema().load(json_data)
    print('Валидация прошла успешно!')
except ValidationError as e:
    print(e)

print(f'Город: {weather.city}')
print(f'Температура: {weather.temperature}°C')
print(f'Описание погоды: {weather.description}')
print(f'Влажность: {weather.humidity}%')
print(f'Скорость ветра: {weather.wind_speed} м/с')
print(f'Видимость: {weather.visibility} км')
