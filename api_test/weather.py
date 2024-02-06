import requests
from .config import get_api_key


KEY_NAME = "OWM_API_KEY"


OWN_API_KEY = get_api_key(KEY_NAME);


URL = "https://api.openweathermap.org/data/2.5/weather"


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
    
    