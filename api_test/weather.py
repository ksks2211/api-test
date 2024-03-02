import requests
from .config import get_api_key

OWN_API_KEY = get_api_key("OWM_API_KEY");

URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_by_lat_and_lon(lat:float, lon:float):
    global OWN_API_KEY
    params = {
        "lat":lat,
        "lon":lon,
        "appid":OWN_API_KEY        
    }
    response = requests.get(URL, params=params)    
    if(response.status_code != 200):
        response.raise_for_status()        
    return response.json()

def get_weather_by_city(city):
    global OWN_API_KEY   
    params = {
        "q":city,
        "appid":OWN_API_KEY,
        "units":"metric"
    }
    response = requests.get(URL, params=params)    
    if(response.status_code != 200):
        response.raise_for_status()        
    return response.json()