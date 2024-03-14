import requests
from bs4 import BeautifulSoup

site_1 = requests.get("https://www.timeout.com/film/best-movies-of-all-time")

site = site_1.text
soup = BeautifulSoup(site, "html.parser")

names = soup.find_all(name="h3", class_="_h3_cuogz_1")

movie_name = [name.getText() for name in names]
movie_name_new = [name.replace("\xa0", '') for name in movie_name]
movie_name_new.pop()


with open("./movies/movies.txt", mode="w") as file:
    for name in movie_name_new:
        file.write(f"{name}\n")