import requests

from classes.weather_response import WeatherResponse


BASE_WEATHER_URL = "http://api.weatherapi.com/v1/current.json"
KEY = "dcf137596441437d9cf171105240604"
AIR_QUALITY = "no"
LANG = "ru"


def lab_13():
    """Узнать погоду для конкретного города"""
    city = input(
        "Погоду для какого города хотите узнать? [London, Moscow, Saint Petersburg]"
    )
    payload = {
        "key": KEY,
        "aiq": AIR_QUALITY,
        "q": city or "Saint Petersburg",
        "lang": LANG,
    }

    r = requests.get(BASE_WEATHER_URL, params=payload, timeout=10)
    r.encoding = "utf-8"
    response_json = WeatherResponse(**r.json())
    location = response_json.location
    current = response_json.current

    print(
        "----------------------------\n"
        f"Город: {location.name} | {current.condition.text}\n"
        f"{int(current.temp_c)}°C (ощущается как {int(current.feelslike_c)}°C)\n"
        f"Видимость: {current.vis_km} км | Широта: {location.lat} | Долгота: {location.lon}\n"
    )


lab_13()
