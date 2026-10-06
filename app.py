from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hei 2IMI!"

@app.route("/om")
def om():
    return "Vi lærer Flask"


if __name__ == "__main__":
    app.run(debug=True)