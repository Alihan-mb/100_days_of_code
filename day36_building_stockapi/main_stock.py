import json
import html
import requests
import datetime as dt
import smtplib
from config import *

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


URL = f"https://www.alphavantage.co/query"
URL_news = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from=2023-12-26&to=2023-12-20&sortBy=popularity&apiKey={API_KEY_NEWS}"


# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day - 1
# day_2 = now.day - 5
#
# date_from_datetime = [str(year), str(month), str(day)]
# date_from_datetime_2 = [str(year), str(month), str(day_2)]
#
# current_day = "-".join(date_from_datetime)
# day_before = "-".join(date_from_datetime_2)

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_STOCK
}

response = requests.get(URL, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
day_before_yesterday = data_list[1]

current_day_open = yesterday_data["1. open"]
day_before_open = day_before_yesterday["1. open"]

difference = float(current_day_open) - float(day_before_open)

diff_percent = round((difference / float(current_day_open)) * 100)
print(diff_percent)
if abs(diff_percent) >= 1:
    news_response = requests.get(URL_news)
    news_response.raise_for_status()
    data_news = news_response.json()["articles"]

    my_email = "alihan-mb@mail.ru"
    to_address = "alihan-mb@list.ru"
    password = "TXmqAexQ4ew07W53pR3j"

    for news in range(3):
        titles = data_news[news]["title"].encode('ascii', 'ignore')
        articles = data_news[news]["description"].encode('ascii', 'ignore')
        news_bank_dict = {titles: articles}

        for key, value in news_bank_dict.items():
            with smtplib.SMTP("smtp.mail.ru", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=to_address,
                    msg=f"Subject: TESLA: The Stock is  {round(diff_percent, 2)}% from the day before. Headline: {key.decode('utf-8')}, \n\n\nBrief: {value.decode('utf-8')}"

                )


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
