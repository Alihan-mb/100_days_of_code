import requests
import random
import json
import string
import pprint

BASE_URL = "https://gorest.co.in"
TOKEN = "Bearer 5d2e569bdbb918a3c1f1357e11f5722f30a75bc85b1c317b6305fb23000b9557"


def generate_randon_email():
    domain = "automation.com"
    email_lenght = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_lenght))
    email = random_string + "@" + domain
    return email


# GET req
def get_request():
    url = BASE_URL + "/public/v2/users/5886987"
    headers = {
        "Authorization": TOKEN
    }
    response = requests.get(url=url, headers=headers)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print(f"Json response body is: {json_str}")
    print("______________________GET REQUEST IS DONE________________________")


# Post req
def post_request():
    url = BASE_URL + "/public/v2/users"
    headers = {
        "Authorization": TOKEN
    }
    data = {
        "name": "Alihan",
        "email": generate_randon_email(),
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url=url, json=data, headers=headers)
    print(response.status_code)
    assert response.status_code == 201

    json_data = response.json()
    response_in_json = json.dumps(json_data, indent=4)
    print(f"Json response body is: {response_in_json}")

    user_id = json_data["id"]
    assert "name" in json_data
    assert json_data["name"] == "Alihan"
    print("________________________POST REQUEST IS DONE______________________")
    return user_id


# Put req
def put_requets(user_id):
    url = BASE_URL + f"/public/v2/users/{user_id}"
    headers = {
        "Authorization": TOKEN
    }
    data = {
        "name": "Alihan Kumar_Ali",
        "email": generate_randon_email(),
        "gender": "male",
        "status": "active"
    }
    response = requests.put(url=url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    response_in_json = json.dumps(json_data, indent=4)
    print(f"Json response body is: {response_in_json}")
    assert json_data["id"] == user_id
    assert json_data["name"] == "Alihan Kumar_Ali"
    print("____________________PUT REQUEST IS DONE_________________________")


# Del req
def delete_request(user_id):
    url = BASE_URL + f"/public/v2/users/{user_id}"
    headers = {
        "Authorization": TOKEN
    }

    response = requests.delete(url=url, headers=headers)
    response.raise_for_status()
    assert response.status_code == 204
    print("____________________DELETE USER IS DONE________________________")


get_request()
user_id = post_request()
put_requets(user_id)
delete_request(user_id)
