import smtplib

import requests

from config import *

my_email = "alihan-mb@mail.ru"
to_address = "alihan-mb@list.ru"
password = "TXmqAexQ4ew07W53pR3j"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
URL_news = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY_STOCK
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)
if abs(diff_percent) > 1:
    news_params = {
        "apiKey": API_KEY_NEWS,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(URL_news, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \n Brief: {article['description']}"
                          for article in three_articles]
    for art in formatted_articles:
        b = art.encode('ascii', 'ignore')
        with smtplib.SMTP("smtp.mail.ru", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_address,
                msg=b.decode("utf-8")

            )