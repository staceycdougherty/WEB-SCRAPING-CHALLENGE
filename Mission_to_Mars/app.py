from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")




@app.route("/")
def index():
    mars_scraped_data = mongo.db.collection.find_one()
    return render_template("index.html", mars=mars_scraped_data)


@app.route("/scrape")
def scrape():
    results = scrape_mars.scrape()
    mongo.db.collection.update({}, results, upsert=True)    
    return redirect("/", code=302)
 

if __name__ == "__main__":
    app.run(debug=True)
