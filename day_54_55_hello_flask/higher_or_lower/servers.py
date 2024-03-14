from flask import Flask
from day_54_55_hello_flask.decorators import *
import random

random_number = random.randint(0, 9)
color_list = ["red", "yellow", "green", "black", "blue", "orange", "purple", "pink", "brown", "grey"]
app = Flask(__name__)
print(random_number)

@app.route("/")
def base_page():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=600>"


@app.route("/<int:number>")
def guessing_number(number):
    if random_number > number:
        return if_low()
    elif random_number < number:
        return if_high()
    else:
        return if_correct()


def if_low():
    return f"<h1 style='color:{random.choice(color_list)}'>Too low, Try again</h1>" \
           "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"


def if_high():
    return f"<h1 style='color:{random.choice(color_list)}'>Too high, Try again</h1>" \
           "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"


def if_correct():
    return f"<h1 style='color:green'>You found it!</h1>" \
           "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
