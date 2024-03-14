#Nesting
capitals = {
  "France": "Paris",
  "Germany": "Berling"
}
#Nest dictionery in a dictionery
travel_log = {
  "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 7},
  "Germany": {"city_names":["Berling", "Hamburg", "Stuttgart"], "total_visits": 4}
}
print(travel_log)
print(travel_log["France"])
print(travel_log["France"]["cities_visited"])
print(travel_log["France"]["total_visits"])

# Nesting dictionary in a List
travel_log = [
  {
    "country":"France",
   "cities_visited":["Paris", "Lille", "Dijon"],
   "total_visits": 7
  },
  {
    "country": "Germany",
   "city_names":["Berling", "Hamburg", "Stuttgart"],
   "total_visits": 4
  }
]

print(travel_log[1]["total_visits"])