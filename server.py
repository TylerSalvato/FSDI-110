from flask import Flask, request
from config import developer, db
import json
from flask_cors import CORS

app = Flask("server")
CORS(app) # warning this line disabling CORS policy


@app.get("/")
def hello():
    return "Hello from Flask"

@app.get("/test")
def test():
    return "Look ma!, I'm a page"

@app.get("/name")
def name():
    return "Tyler Salvato"




###################################
######### Products API ############
###################################


def fix_id(record):
    record["_id"] = str(record["_id"])
    return record



@app.get("/api/about")
def about_me():
    return json.dumps(developer)



# get /api/products
# send the list of products
@app.get("/api/products")
def get_products():
    products = []

    cursor = db.products.find({})
    for prod in cursor:
        products.append(fix_id(prod))


    return json.dumps(products)



@app.post("/api/products")
def save_products():
    # read the payload/body from the http request
    product = request.get_json()

    db.products.insert_one(product)

    print(product) # print to console

    return json.dumps(fix_id(product))


@app.get("/api/categories")
def get_categories():
    #return a list of your categories
    cursor = db.products.find({})

    categories = []

    for prod in cursor:
        cat = prod["category"]
        if cat not in categories:
            categories.append(cat)

    categories.sort()
    return json.dumps(categories)



@app.get("/api/products/<category>")
def get_by_category(category):
    products = []
    cursor = db.products.find({"category": category})

    for prod in cursor:
        products.append(fix_id(prod))

    return json.dumps(products)


app.run(debug=True)
