from flask import Flask, render_template
from flask_pymongo import PyMongo
import os
import sys
import Challenge_Solution
import requests
#from flask import request
import urllib.request
from PIL import Image
import os, os.path
import glob
from flask import send_file, send_from_directory, safe_join, abort

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/challenge_mars_db"
mongo = PyMongo(app)

@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("challenge_index.html", mars=mars)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = Challenge_Solution.scrape_hemisphere()
   mars.update({}, mars_data, upsert=True)
   return "Scraping Successful!"

@app.route("/home")
def home_page():
   return "Welcome to Mars Hemispheres home page!!!"

@app.route("/thumbnails")
def thumbnails():
   mars = mongo.db.mars
   hemisphere_data = mars.find_one()
   mars_list = hemisphere_data.get('mars_hemisphere_details')
   
   items = [doc[1] for doc in mars_list]
   i=0
   for item in items:
         filename = f"/Users/macuser/Documents/DataAnalysis/Mission-to-Mars/thumbnails/{i}.jpg"
         f = open(filename,'wb')
         f.write(requests.get(item).content)
         f.close()
         i+=1
         #urllib.request.urlopen(item)
   #image_list = []
   '''for filename in glob.glob('/Users/macuser/Documents/DataAnalysis/Mission-to-Mars/thumbnails/*.jpg'): #assuming jpg
      im=Image.open(filename)
      im.show()
      image_list.append(im)'''
      #return send_file()
   return render_template("thumbnail_index.html", items=items)


if __name__ == "__main__":
   app.run()