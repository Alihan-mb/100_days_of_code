import time

import requests
from datetime import datetime
import smtplib

my_email = "alihan-mb@mail.ru"
password = "TXmqAexQ4ew07W53pR3j"

MY_LAT = 48.686530  # Your latitude
MY_LONG = 46.867390  # Your longitude

def is_iss_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude < MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def checking_if_time_right():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "tzId": "Europe/Moscow",
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if sunrise > time_now > sunset:
        return True


while True:
    print(f"The loop started at {datetime.now()}")
    time.sleep(60)
    if is_iss_above() and checking_if_time_right():
        with smtplib.SMTP("smtp.mail.ru", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)

            connection.sendmail(
                from_addr=my_email,
                to_addrs="alihan-mb@list.ru",
                msg="Subject: ISS is above you! \n\n\nGo outside and look at the sky, the international "
                    "space station is above you"
            )
            print("message was sent")


