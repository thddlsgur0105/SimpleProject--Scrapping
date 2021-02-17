from flask import Flask, render_template, send_file
from scrapper import getResults
from exporter import save_to_file

app = Flask("News_Scrapper")
fakeData = {}

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/report")
def report():
  DB = getResults()
  fakeData["DB"] = DB
  return render_template("result.html", typeNumber = len(DB), db = DB)

@app.route("/export")
def export():
  save_to_file(fakeData["DB"])
  return send_file("news.csv")


app.run(host="0.0.0.0")