from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    print("Good health everyone")
    return "Good health everyone"


if __name__ == "__main__":
    app.run(debug=True)