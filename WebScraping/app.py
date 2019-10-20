# import necessary libraries
from flask import Flask, render_template, jsonify, redirect
import pymongo
import mission_to_mars

# create instance of Flask app
app = Flask(__name__)

# open Database
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.marsdata
mars = list(db.mars_data.find())

#  create route that renders index.html template
@app.route("/")
def index():
    #mars = db.mars_data.find()
    return render_template("index.html", mars=mars)
    #return render_template("index.html")


@app.route("/scrape")
def scrape():
    mars = db.mars_data
    mars_df = mission_to_mars.scrape()
     
    mars.update(
        {},
        mars_df,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)