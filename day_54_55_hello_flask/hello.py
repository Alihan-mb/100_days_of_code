from flask import Flask
from decorators import *

app = Flask(__name__)

print(__name__)
@app.route("/")
def hello_world():
    return '<h1 style="text-align: center; color:red">Hello, World!</h1>'\
            '<p>This is another paragraph</p>'\
           '<img src="https://media.giphy.com/media/3o7527pa7qs9kCG78A/giphy.gif" width=200>'


@app.route("/bye")
@make_underlined
@make_emphasis
@make_bold
def bye():
    return "Bye"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, your place in line is {number}"

if __name__ == "__main__":
    app.run(debug=True)