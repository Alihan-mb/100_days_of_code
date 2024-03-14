import requests

p = {
    "page": 2
}

resp = requests.get("https://reqres.in/api/users", params=p)

json_resp = resp.json()


assert json_resp["total"] == 12
assert json_resp["total_pages"] == 2, "total pages count is not matching"

email = json_resp["data"][2]["email"]
assert email.endswith("reqres.in"), "it does not end like that "

first_name = json_resp["data"][2]["first_name"]

assert first_name == "Tobias"

print(json_resp["support"]["url"])