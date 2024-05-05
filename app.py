from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# MySQL Configuration
config = {
  'user': 'root',
  'password': '2004',
  'host': 'localhost',
  'database': 'cloudy_members',
  'port': 3306,
  'cursorclass': pymysql.cursors.DictCursor
}

cnx = pymysql.connect(**config)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/team")
def team():
    with cnx.cursor() as cursor:
        cursor.execute("SELECT * FROM team")
        data = cursor.fetchall()
    return render_template("team.html", team=data)

if __name__ == "__main__":
    app.run(debug=True)
