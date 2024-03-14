import requests
from bs4 import BeautifulSoup


user_data = input("Which year would you like to travel to? Type the data in this format YYYY-MM-DD ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_data}")
soup = BeautifulSoup(response.text, "html.parser")

songs = soup.select("li ul li h3")

song_titles = [song.getText().strip() for song in songs]
