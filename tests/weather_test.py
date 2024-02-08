from api_test.common import save_dict_as_json
from api_test.weather import get_weather_by_city

city = "New York"
location = './tests/nyc_weather.json'

response = get_weather_by_city(city)

if response is not None:
    save_dict_as_json(data=response, location=location)