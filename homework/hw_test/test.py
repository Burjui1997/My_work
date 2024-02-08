import pytest

from hw_30 import WeatherRequest


@pytest.fixture
def weather_request():
    return WeatherRequest()


@pytest.mark.parametrize("city_name", ['Москва'])
def test_weather_request_city_name(weather_request, city_name):
    response = weather_request.get_weather(city_name)  # Передаем название города в метод get_weather
    assert response['name'] == city_name  # Проверяем, что имя города в ответе соответствует ожидаемому


@pytest.mark.parametrize("city, expected_coords", [
    ('Москва', {"lon": 37.6156, "lat": 55.7522}),
    ('Воронеж', {"lon": 39.17, "lat": 51.6664}),
    ('Санкт-Петербург', {"lon": 30.2642, "lat": 59.8944}),
    ('Краснодар', {"lon": 38.9769, "lat": 45.0328}),
    ('Сочи', {"lon": 39.7303, "lat": 43.6}),
])
def test_weather_request_coord(weather_request, city, expected_coords):
    response = weather_request.get_weather(city)
    coords = {"lon": response['coord']['lon'], "lat": response['coord']['lat']}
    assert coords == expected_coords


@pytest.mark.parametrize("city, expected_coords", [
    ('Москва', {"lon": 37.6156, "lat": 55.7522}),
    ('Воронеж', {"lon": 39.17, "lat": 51.6664}),
    ('Санкт-Петербург', {"lon": 30.2642, "lat": 59.8944}),
    ('Краснодар', {"lon": 38.9769, "lat": 45.0328}),
    ('Сочи', {"lon": 39.7303, "lat": 43.6}),
])
def test_weather_request_weather_key(weather_request, city, expected_coords):
    response = weather_request.get_weather(city)
    weather_info = response['weather']

    for item in weather_info:
        assert all(key in item for key in ["id", "main", "description", "icon"])


@pytest.mark.parametrize("city, expected_coords", [
    ('Москва', {"lon": 37.6156, "lat": 55.7522}),
    ('Воронеж', {"lon": 39.17, "lat": 51.6664}),
    ('Санкт-Петербург', {"lon": 30.2642, "lat": 59.8944}),
    ('Краснодар', {"lon": 38.9769, "lat": 45.0328}),
    ('Сочи', {"lon": 39.7303, "lat": 43.6}),
])
def test_weather_request_main_key(weather_request, city, expected_coords):
    response = weather_request.get_weather(city)
    main_info = response['main']

    assert all(key in main_info for key in ["temp", "feels_like", "temp_min", "temp_max", "pressure", "humidity"])


@pytest.mark.parametrize("city, expected_coords", [
    ('Москва', {"lon": 37.6156, "lat": 55.7522}),
    ('Воронеж', {"lon": 39.17, "lat": 51.6664}),
    ('Санкт-Петербург', {"lon": 30.2642, "lat": 59.8944}),
    ('Краснодар', {"lon": 38.9769, "lat": 45.0328}),
    ('Сочи', {"lon": 39.7303, "lat": 43.6}),
])
@pytest.mark.slow
def test_weather_request_city_coodrd_name_parametrize_slow(weather_request, city, expected_coords):
    response = weather_request.get_weather(city)

    assert response['name'] == city
    assert response['coord']['lat'] == pytest.approx(expected_coords["lat"], abs=0.001)
    assert response['coord']['lon'] == pytest.approx(expected_coords["lon"], abs=0.001)
