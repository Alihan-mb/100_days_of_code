import smtplib
import pandas
import datetime as dt
import random

my_email = "alihan-mb@mail.ru"
password = "TXmqAexQ4ew07W53pR3j"

data = pandas.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")

now = dt.datetime.now()
month = now.month
day = now.day

ran_int = random.randint(1, 3)

for bd in birthdays:
    if bd["month"] == month and bd["day"] == day:
        with open(f"letter_{ran_int}.txt", newline="\n") as file:
            letter_content = file.read()
            letter_content = letter_content.replace("[NAME]", bd["name"])

            with smtplib.SMTP("smtp.mail.ru", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)

                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=bd["email"],
                    msg=f"Subject: Happy Birthday, \n\n\n{letter_content}"
                )
















            #
            # with smtplib.SMTP("smtp.mail.ru", port=587) as connection:
            #     connection.starttls()
            #     connection.login(user=my_email, password=password)
            #
            #     connection.sendmail(
            #         from_addr=my_email,
            #         to_addrs=bd["email"],
            #         msg=f"Subject: Happy Birthday!!! \n\n{letter_content}")
