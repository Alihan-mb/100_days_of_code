import requests
from datetime import datetime

# url = "http://api.open-notify.org/iss-now.json"
# response = requests.get(url=url)
# response.raise_for_status()
# data = response.json()
#
# print(data)
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

url = "https://api.sunrise-sunset.org/json"

lat_and_long = {
    "lat": "42.686530",
    "lng": "46.867390",
    "tzId": "Europe/Moscow",
    "formatted": 0
}

response = requests.get(url=url, params=lat_and_long)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)


time_now = datetime.now()
print(time_now.hour)