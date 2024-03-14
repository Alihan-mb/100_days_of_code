import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "alihan-mb@mail.ru"
password = "TXmqAexQ4ew07W53pR3j"

url = "https://www.lamoda.ru/p/rtladc678001/clothes-karllagerfeld-plate/?source_rec_type=mainpage"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")

product = soup.select("div div div div span")

a = [f.get_text(strip=True) for f in product]

product_price = int(a[3].replace("₽", "").replace(" ", ""))

message = "Subject: Price of the dress \n\n\nHey, the price of the dress is finally bellow 27000"
if product_price < 30000:
    with smtplib.SMTP("smtp.mail.ru", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="alihan-mb@list.ru",
            msg=message
        )


















