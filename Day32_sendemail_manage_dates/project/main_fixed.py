import smtplib
import pandas
import datetime as dt
import random

ran_int = random.randint(1, 3)

my_email = "alihan-mb@mail.ru"
password = "TXmqAexQ4ew07W53pR3j"

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row["day"], row["month"]): row for (index, row) in data.iterrows()}
print(birthdays_dict)
now = dt.datetime.now()
today = (now.day, now.month)

if today in birthdays_dict:
    birthdays_person = birthdays_dict[today]
    with open(f"letter_{ran_int}.txt") as f:
        content = f.read()
        letter_to_send = content.replace("[NAME]", birthdays_person["name"])

    with smtplib.SMTP("smtp.mail.ru", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthdays_person["email"],
            msg=f"Subject: Happy Birthday!!! \n\n{letter_to_send}")
