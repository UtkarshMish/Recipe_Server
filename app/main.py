import hashlib
import os

import jwt
import pymongo
from dotenv import load_dotenv, find_dotenv
from flask import Flask, jsonify, request, render_template, send_file
from flask_cors import CORS
from pymongo import ReturnDocument

from Recipe_Model import Recommender

# import json

app = Flask(__name__)
load_dotenv(find_dotenv())

KEY = os.getenv("KEY")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
client = pymongo.MongoClient(
    f"mongodb+srv://{KEY}:{PASSWORD}@{HOST}/test?retryWrites=true&w=majority")
db = client["Recipe"]
user = db["Users"]
Cuisines = db["Cuisines"]
# Common Response
TRUE = {"value": True}
FALSE = {"value": False}
EXIST = {"value": "exist"}
RECIPE_SCHEMA = {
    "_id": 0,
    "id": 1,
    "name": 1,
    "ingredients": 1,
    "description": 1,
    "nutrition": 1,
    "serving_count": 1,
    "ratings": 1,
    "breadcrumbs": 1,
    "img_link": 1,
    "total_time": 1,
}


def get_next_sequence(collection, name):
    return collection.find_one_and_update(
        {
            name: name
        }, {
            '$inc': {
                'seq': 1
            }
        },
        projection={
            'seq': True,
            '_id': False
        },
        return_document=ReturnDocument.AFTER).get("seq")


def get_token(users):
    encoded_jwt = jwt.encode({
        "password": users["password"]
    },
                             "project",
                             algorithm="HS256").decode("UTF-8")

    return encoded_jwt


def get_recommend(cuisines, result_data):
    recommender = Recommender(cuisines, result_data)
    return recommender.user_like_recommend()


@app.route("/robots.txt")
def robots():
    return send_file("./static/react/robots.txt")


@app.route("/sitemap.xml")
def sitemap():
    return send_file("./sitemap.xml")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def recipe_advisor(path=None):
    return render_template("index.html")


@app.route("/api/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        users = dict(request.get_json())

        if users["email"]:
            users["email"] = str(users["email"]).lower()
            users["password"] = hashlib.sha1(
                users["password"].encode()).hexdigest()
            result = user.find_one(users)
            if result:
                encoded_jwt = get_token(users)
                return {
                    "username": result["user_name"],
                    "value": "true",
                    "token": encoded_jwt,
                }
            else:
                return FALSE
    return FALSE


@app.route("/api/signup", methods=["GET", "POST"])
def signup():
    print(request.environ["REMOTE_ADDR"])
    if request.method == "POST":
        users = dict(request.get_json())
        users["user_name"] = users["user_name"].capitalize()
        if users["email"]:
            users["email"] = str(users["email"]).lower()
            users["password"] = hashlib.sha1(
                users["password"].encode()).hexdigest()
            result = user.find_one({"email": users["email"]}) or 0
            if result != 0:
                return EXIST
            else:
                encoded_jwt = get_token(users)
                users["id"] = get_next_sequence(db.orgid_counter, 'user_id')
                user.insert_one(users)
                return {
                    "username": users["user_name"],
                    "value": "success",
                    "token": encoded_jwt,
                }
    return FALSE


@app.route("/api/verify-token", methods=["GET", "POST"])
def check_api():
    if request.method == "POST":
        user_data = request.get_json()
        token = user_data["token"]
        if not token:
            return FALSE
        else:
            token = bytes(token, encoding="UTF-8")
            try:
                password = jwt.decode(token, "project", algorithms=["HS256"])
            except:
                return FALSE
            result = user.find_one(password) or 0
            if result != 0:
                return TRUE
            else:
                return FALSE
    return FALSE


@app.route("/api/get-recipe/<int:page_no>", methods=["GET", "POST"])
def get_cuisine(page_no=0):
    page_no = int(page_no)
    if page_no > 0:
        page_size = 6
        limit = page_size * page_no
        recipe_data = [
            recipe for recipe in Cuisines.find(
                projection=RECIPE_SCHEMA).skip(limit -
                                               page_size).limit(page_size)
        ]
        recipe_data.append(
            {"totalSize": Cuisines.estimated_document_count() + 1})
        return jsonify(recipe_data)
    return FALSE


@app.route("/api/recipe/<int:recipe_id>", methods=["GET", "POST"])
def get_recipe(recipe_id=0):
    recipe_id = int(recipe_id)
    if recipe_id > 0:
        recipe_data = Cuisines.find_one({"id": recipe_id},
                                        projection=RECIPE_SCHEMA)
        if recipe_data:
            return jsonify(recipe_data)
    return FALSE


@app.route("/api/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query_request = request.get_json() or 0
        if query_request != 0:
            page_no = query_request['page_no']
            page_size = 6
            limit = page_size * page_no
            query_value = "".join([
                ch for ch in query_request['query']
                if ch.isalpha() or ch == ' '
            ])
            query_result = [
                cuisine for cuisine in Cuisines.find(
                    {
                        'name': {
                            '$regex': f".*{query_value}.*",
                            '$options': 'i'
                        }
                    },
                    projection=RECIPE_SCHEMA).skip(limit -
                                                   page_size).limit(page_size)
            ]
            query_result.append({
                "totalSize":
                Cuisines.find({
                    'name': {
                        '$regex': f".*{query_value}.*",
                        '$options': 'i'
                    }
                }).count()
            })
            return jsonify(query_result)
        return TRUE
    return FALSE


@app.route("/api/predict", methods=["GET", "POST"])
def predict_recipe():
    if request.method == 'POST':
        data = request.get_json()
        query = data['queryString']
        if len(query) > 0:
            query = " ".join(query).lower()
            cuisine_list = [
                cuisine for cuisine in Cuisines.find(projection=RECIPE_SCHEMA)
            ]
            recipe = Recommender(cuisine_list, query)
            predicted_id = recipe.guide_predictor()
            recipe_data = [
                recipe for recipe in Cuisines.find(
                    {"id": {
                        "$in": predicted_id
                    }}, projection=RECIPE_SCHEMA)
            ]
            if len(recipe_data) > 0:
                return jsonify(recipe_data)
    return FALSE


@app.route("/api/userLikings", methods=["GET", "POST"])
def user_likes():
    if request.method == "POST":
        user_data = request.get_json()
        password = user_data["token"]
        if not password:
            return FALSE
        else:
            token = bytes(password, encoding="UTF-8")
            try:
                password = jwt.decode(token, "project", algorithms=["HS256"])
            except:
                return FALSE
            result = user.find_one({
                "user_name": user_data['user'],
                "password": password['password']
            }) or 0
            if result != 0 and user_data['recipe_id'] is None:
                result_data = db['LikedRecipe'].find_one(
                    {"user_id": result['id']},
                    projection={
                        '_id': False,
                        'liked_recipe': True
                    })
                if result_data is not None and user_data['recommendation']:
                    result_data = liked_response(result_data)
                    return result_data
                elif result_data:
                    return result_data
                else:
                    return FALSE
            if result != 0:
                operation = '$push' if user_data['liked'] else '$pull'
                success = db['LikedRecipe'].find_one_and_update(
                    {"user_id": result['id']},
                    {operation: {
                        'liked_recipe': user_data['recipe_id']
                    }},
                    return_document=ReturnDocument.AFTER)
                if not success:
                    success = db['LikedRecipe'].insert_one({
                        "user_id":
                        result['id'],
                        "liked_recipe": [int(user_data['recipe_id'])]
                    })
                if success:
                    return TRUE
            else:
                return FALSE
    return FALSE


def liked_response(result_data):
    cuisines = list(Cuisines.find(projection={'_id': False}).sort('id'))
    liked = result_data['liked_recipe'] or []
    result_data['liked_recipe'] = [
        recipe for recipe in cuisines if recipe['id'] in liked
    ]
    result_data['recommendations'] = get_recommend(cuisines, liked)
    return result_data


if __name__ == "__main__":
    # with open("./data/cleaned_data.json") as recipe_data:
    #     recipes = json.load(recipe_data)
    #     Cuisines.insert_many([recipe for recipe in recipes])
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.run()
