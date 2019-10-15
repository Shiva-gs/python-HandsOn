# import necessary libraries
from flask import Flask, render_template
import requests
import json
import pandas as pd
import pymongo

# create instance of Flask app
app = Flask(__name__)

# List of dictionaries
index_price = db.index_price.find()
data = pd.DataFrame(list(index_price))
 

    
dict_data = data.to_dict
dict_data

# create route that renders index.html template
@app.route("/")
def index():

    return render_template("index.html", dict_data=dict_data)


if __name__ == "__main__":
    app.run(debug=True)