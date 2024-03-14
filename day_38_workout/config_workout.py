import os
from pprint import pprint

APIKEY = "adc659fd2c9e7d114aece0eedb049e27"
APPID = "e78cbe19"
HOST = "https://trackapi.nutritionix.com"
ENDPOINT = "/v2/natural/exercise"
Content_type = "application/json"

GOOGLE_SHEET_API = "1dm9CaK8_G8Uc7i7B3kzEXSdqs9DyMApSBebuipRuvnQ"
GOOGLE_SHEET_URL = "https://api.sheety.co/e5d019090d15a1aad8a88f28614c690b/myWorkoutsMine/workouts"

TOKEN = "SpartakAli"
BASIC = "QWxpaGFuOk1hcnNpYW5pbg=="

os.environ["APPID"] = APPID
os.environ["APIKEY"] = APIKEY
os.environ["HOST"] = HOST
os.environ["ENDPOINT"] = ENDPOINT
os.environ["Content_type"] = Content_type
os.environ["GOOGLE_SHEET_API"] = GOOGLE_SHEET_API
os.environ["GOOGLE_SHEET_URL"] = GOOGLE_SHEET_URL
os.environ["TOKEN"] = TOKEN

env_var = os.environ

