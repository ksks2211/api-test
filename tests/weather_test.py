from api_test.common import save_dict_as_json
from api_test.weather import get_weather_by_city, get_weather_by_lat_and_lon
from api_test.common import current_datetime_mod




today = current_datetime_mod()
location = f'./tests/tokyo_weather-{today}.json'

lat=35.6895
lon=139.6917

response = get_weather_by_lat_and_lon(lat,lon)




if response is not None:
    save_dict_as_json(data=response, location=location)