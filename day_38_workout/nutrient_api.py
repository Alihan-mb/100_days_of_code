import requests
import config_workout as conf

class Nutrient:
    def __init__(self, apikey, appid, applicaton_type):
        self.apikey = apikey
        self.appid = appid
        self.application_type = applicaton_type

    def nutrient_post_exercise(self, query):
        nutrient_headers = {
            "Content-type": self.application_type,
            "x-app-id": self.appid,
            "x-app-key": self.apikey
        }
        nutrient_body = {
            "query": query,
            "gender": "male",
            "weight_kg": 80,
            "height_cm": 167,
            "age": 26
        }

        nutrient_response = requests.post(url=f"{conf.HOST}{conf.ENDPOINT}", json=nutrient_body, headers=nutrient_headers)
        return nutrient_response