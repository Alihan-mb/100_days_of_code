import requests
import datetime as dt

pixela_endpoint = " https://pixe.la/v1/users"

USERNAME = "alikhanmagomedaliev"
TOKEN = "marsianin_ali_123_pp"
GRAPHID = "graph1"

user_params = {
    "token": "marsianin_ali_123_pp",
    "username": "alikhanmagomedaliev",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_header = {
    "X-USER-TOKEN": TOKEN,
}

graph_config = {
    "id": GRAPHID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji",
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_header)
# print(response.json())



now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
date_from_datetime = [str(year), str(month), str(day)]

current_day = "".join(date_from_datetime)


posting_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}"
#
# response_pixel = requests.post(url=posting_pixel_endpoint, json=pixel_config, headers=pixel_header)
# print(response_pixel.text)

# yesterday = dt.datetime(year=2023, month=12, day=27)
# formatted_yesterday = yesterday.strftime("%Y%m%d")

# put_url = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{formatted_yesterday}"
#
# update_date = {
#     "quantity": "27.5",
# }
#
# response_update = requests.put(url=put_url, json=update_date, headers=pixel_header)
# print(response_update.text)
#
# delete_url = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{formatted_yesterday}"
# delete_resp = requests.delete(url=delete_url, headers=pixel_header)
# print(delete_resp.text)











