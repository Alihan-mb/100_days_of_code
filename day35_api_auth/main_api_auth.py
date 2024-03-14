import requests

APIKEY = "1a7dac74077fbadb916818a72788c51d"
URL = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": "42.686531",
    "lon": "46.867390",
    "appid": APIKEY,
    "cnt": 4,
}

response = requests.get(URL, params=parameters)
response.raise_for_status()

weather_data = response.json()["list"]

will_raine = False
for id in range(4):
    weather_id = weather_data[id]["weather"][0]["id"]
    if weather_id < 700:
        will_raine = True

'''Angela's solution'''
# for id in weather_data: #weather_data is a list
#     weather_id = id["weather"][0]["id"]
#     if weather_id < 700:
#         will_raine = True

if will_raine:
    url = "https://phonenumbervalidatefree.p.rapidapi.com/ts_PhoneNumberValidateTest.jsp"

    querystring = {
        "number": "+79880604983",
        "country": "RU"
    }

    headers = {
        "X-RapidAPI-Key": "de5e257895msh5178e7be429c8f6p16151cjsn34999f203610",
        "X-RapidAPI-Host": "phonenumbervalidatefree.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())