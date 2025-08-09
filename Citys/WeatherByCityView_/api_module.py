import threading
import requests
from .matches.get_best_match import GetBestMatch
from .secret import API_KEY, BASE_URL, LIST_FILE_PATH

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
