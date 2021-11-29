from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
# import scraping
# import Train

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/predict")
# def predict(data):
#     result = predict_fucntion(data)
#     return render_template("index.html", something=result)

@app.route("/record", methods=['GET', 'POST'])
def record():
    print("record")
#     voice_data = scraping.scrape_all()
#     mars.update({}, mars_data, upsert=True)
    return render_template("mic.html")

if __name__ == "__main__":
    app.run()
