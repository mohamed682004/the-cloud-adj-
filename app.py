from flask import Flask, render_template

app = Flask(__name__)


# Not implemented
@app.route("/")
def home():
    return render_template("index.html")


# Not implemented
@app.route("/team")
def team():
    return render_template("team.html")


if __name__ == "__main__":
    app.run(debug=True)
