import threading
import requests
from .matches.get_best_match import GetBestMatch

API_KEY = "0ac0279ee0c026f781b30a8d26752d9a"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
LIST_FILE_PATH = "Citys/WeatherByCityView_/matches/city_aliases.json"

def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    with requests.get(BASE_URL, params=params) as resp:
        data = resp.json()
        return {city: data}

def result(city_):
    city_name = GetBestMatch(city_, LIST_FILE_PATH).get()['matched_string']
    object_ = fetch_weather(city_name)
    result_ = object_
    return result_
