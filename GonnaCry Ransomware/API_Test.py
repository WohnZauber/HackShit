import requests
import json
from datetime import datetime
import pytz

def get_weather(api_key, city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    data = response.json()

    if data.get("main"):
        main = data["main"]
        temperature = main["temp"]
        humidity = main["humidity"]
        weather_desc = data["weather"][0]["description"]

        print(f"Temperature : {temperature - 273.15}°C")
        print(f"Humidity : {humidity}%")
        print(f"Weather description : {weather_desc}")

        if data.get("timezone"):
            timezone = pytz.timezone(pytz.country_timezones[data["sys"]["country"]][0])
            city_time = datetime.now(timezone)
            formatted_time = city_time.strftime("%H:%M:%S")
            formatted_date = city_time.strftime("%d.%m.%Y")
            print(f"City date : {formatted_date}")
            print(f"City time : {formatted_time}")
    else:
        print(data)

if __name__=="__main__":
    api_key = "d2e29cbce206b2652ecd49743a590fad"
    city = "Warngau"
    get_weather(api_key, city)