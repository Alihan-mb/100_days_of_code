import os

import requests
import config_workout as conf
from day_38_workout.nutrient_api import Nutrient
import datetime as dt
from day_38_workout.sheet_api import Sheet_api

nutrient = Nutrient(os.environ["APIKEY"], conf.APPID, conf.Content_type)
google_sheet = Sheet_api(conf.GOOGLE_SHEET_URL)

user_exercise = input("What exercise/exercises you did? ")
response_nutrient = nutrient.nutrient_post_exercise(user_exercise)

calories = response_nutrient.json()["exercises"][0]["nf_calories"]
duration = response_nutrient.json()["exercises"][0]["duration_min"]

today = dt.datetime.now()
formatted_date = today.strftime("%d/%m/%Y")
formatted_time = today.strftime("%H:%M:%S")

response_google_sheet = google_sheet.updating_sheet(formatted_date=formatted_date,
                                                    formatted_time=formatted_time,
                                                    user_exercise=user_exercise,
                                                    duration=duration,
                                                    calories=calories)

response_google_sheet.raise_for_status()















