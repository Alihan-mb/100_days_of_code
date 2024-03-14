import requests
from bs4 import BeautifulSoup
import re

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

resp = requests.get(URL)
soup = BeautifulSoup(resp.text, "html.parser")

movies = soup.find_all(name="h3", class_="title")
movies_list = [movie.getText() for movie in movies]

movie_reversed = movies_list[::-1]
print(movie_reversed)

with open("./movies/movies.txt", mode="w") as file:
    for mov in movie_reversed:
        clean_string = re.sub(r'[^\x00-\x7F]+', '',mov)
        file.write(f"{clean_string}\n")