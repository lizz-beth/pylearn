import json
from requests import request

from errors import WeatherFetchError

url = "https://community-open-weather-map.p.rapidapi.com/weather"

headers = {
    'x-rapidapi-key': "34ecd36a90msh94f6ca3f9b9c982p186fb3jsn8f6633ce8cfb",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
}


def weather_data(query):

    response = request("GET", url, headers=headers, params=query)

    if not response.ok:
        raise WeatherFetchError(response.json()["message"])

    response_json = json.loads(response.text[5:-1])

    main_data = response_json["main"]

    return {
        "Город": "\t" + response_json["name"],
        "Описание": response_json["weather"][0]["description"],
        "Температура": "{} °C".format(main_data["temp"]),
        "Ощущается": main_data["feels_like"],
        "Атм. давление": "{} мм.рт.с.".format(main_data["pressure"]),
        "Скорость ветра": "{} м/c ".format(response_json["wind"]["speed"])
    }
