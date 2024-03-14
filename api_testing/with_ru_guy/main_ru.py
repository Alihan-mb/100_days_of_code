import requests
# from apikey import API
#
# URL = "https://api.openweathermap.org/data/2.5/forecast"
#
# parameters = {
#     "lat": "42.686531",
#     "lon": "46.867390",
#     "appid": API,
#     "cnt": 4,
# }
#
# response = requests.get(URL, params=parameters)
#
# response.raise_for_status()
# print(response.status_code)
# print(response.headers)
# print(response.text)

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru,en;q=0.9,en-US;q=0.8",
    "Host": "httpbin.org",
    "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}
#
#
#
# resp = requests.get(url="https://httpbin.org/headers", headers=headers)
# print(resp.text)
# print(resp.headers)

data = {
    "custname": "логин",
    "custtel": "2555",
    "custemail": "test@test.ru",
    "size": "small",
    "delivery": "",
    "comments": ""
}

session = requests.Session()


token = session.get("https://httpbin.org/forms/post")
resp = session.post(url="https://httpbin.org/post", headers=headers, data=data)
print(resp.text)




















