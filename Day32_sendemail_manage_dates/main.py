import smtplib
import datetime as dt
import random

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
now = dt.datetime.now()
week_day = days[now.weekday()]

with open("quotes.txt", encoding="utf8") as file:
    data = file.read().splitlines()

random_quote = random.choice(data).strip().encode("ascii", "ignore")
quote = random_quote.decode("utf-8", "ignore")

subject = f"This is your quote for {week_day}"
message = f"Subject: {subject}\n\n{quote}"


my_email = "alihan-mb@mail.ru"
password = "TXmqAexQ4ew07W53pR3j"

with smtplib.SMTP("smtp.mail.ru", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    connection.sendmail(
        from_addr=my_email,
        to_addrs="alihan-mb@list.ru",
        msg=message)
