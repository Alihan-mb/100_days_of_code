import requests
import config_workout as conf
from requests.auth import HTTPBasicAuth


class Sheet_api:

    def __init__(self, url):
        self.url = url

    def updating_sheet(self, formatted_date, formatted_time, user_exercise, duration, calories):
        google_sheet_body = {
            "workout": {
                "date": formatted_date,
                "time": formatted_time,
                "exercise": user_exercise,
                "duration": duration,
                "calories": calories
            }
        }
        # header = {
        #     "Authorization": f"Bearer {conf.TOKEN}"
        # }

        basic = HTTPBasicAuth("Alihan", "Marsianin")
        response = requests.post(url=self.url, json=google_sheet_body, auth=basic)

        return response
