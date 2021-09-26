import hashlib
from typing import Any, Dict, List, Optional

from beanie.odm.documents import Document
from flask.json import JSONEncoder
import jwt
from dotenv import load_dotenv, find_dotenv
from flask import Flask, jsonify, request, render_template, send_file
from flask_cors import CORS
from pydantic.types import Json
from pymongo import ReturnDocument
from app.models import LikedRecipe, Recipe, User, UserQuery
from Recipe_Model import Recommender
from app.Database import init
from beanie import PydanticObjectId

load_dotenv(find_dotenv())


class JSONEncoderImproved(JSONEncoder):
    '''
        Used to Properly parse ObjectId
        '''
    def default(self, obj):
        if isinstance(obj, PydanticObjectId):
            return str(obj)
        elif isinstance(obj, Document):
            return obj.dict()
        else:
            return JSONEncoder.default(self, obj)


app = Flask(__name__)
app.json_encoder = JSONEncoderImproved

# Common Response
TRUE = {"value": True}
FALSE = {"value": False}
EXIST = {"value": "exist"}


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
    encoded_jwt = jwt.encode({"password": users["password"]},
                             "project",
                             algorithm="HS256")

    return encoded_jwt


def get_recommend(cuisines: List[Recipe], result_data: Optional[Dict[str,
                                                                     Any]]):
    recommender = Recommender([cusine.dict() for cusine in cuisines],
                              result_data)
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


@app.post("/api/login")
async def login():
    await init()
    users = dict(request.get_json())
    if users["email"]:
        users["email"] = str(users["email"]).lower()
        users["password"] = hashlib.sha1(
            users["password"].encode()).hexdigest()
        result = await User.find_one(User.email == users["email"])
        if result and result.password == users["password"]:
            encoded_jwt = get_token(users)
            return {
                "username": result.user_name,
                "value": "true",
                "token": encoded_jwt,
            }
    return FALSE


@app.post("/api/signup")
async def signup():
    await init()
    users = dict(request.get_json())
    users["user_name"] = users["user_name"].capitalize()
    if users["email"]:
        users["email"] = str(users["email"]).lower()
        users["password"] = hashlib.sha1(
            users["password"].encode()).hexdigest()
        result = await User.find_one(User.email == users["email"])
        if result:
            return EXIST
        else:
            encoded_jwt = get_token(users)
            try:
                await User(user_name=users["user_name"],
                           email=users["email"],
                           password=users["password"]).create()
                return {
                    "username": users["user_name"],
                    "value": "success",
                    "token": encoded_jwt,
                }
            except Exception:
                return {"username": users["user_name"], "value": "failed"}
    return FALSE


@app.post("/api/verify-token")
async def check_api():
    await init()
    user_data = request.get_json()
    token = user_data["token"]
    if not token:
        return FALSE
    else:
        token = bytes(token, encoding="UTF-8")
        try:
            password: str = jwt.decode(token, "project",
                                       algorithms=["HS256"])["password"]
            result = await User.find_one(User.password == password)
            return TRUE if result else FALSE
        except Exception:
            return FALSE


@app.route("/api/get-recipe/<int:page_no>", methods=["GET", "POST"])
async def get_cuisine(page_no=0):
    await init()
    page_no = int(page_no)
    if page_no > 0:
        page_size = 6
        limit = page_size * page_no
        recipe_data = await Recipe.all().skip(limit - page_size).limit(
            page_size).to_list()

        recipe_data.append({"totalSize": await Recipe.count() + 1})
        return jsonify(recipe_data)
    return FALSE


@app.get("/api/recipe/<string:recipe_id>")
async def get_recipe(recipe_id):
    await init()
    recipe_data = await Recipe.get(recipe_id)
    return jsonify(recipe_data) if recipe_data else FALSE


@app.post("/api/search")
async def search():
    await init()
    query_request = request.get_json()
    if query_request:
        page_no = query_request['page_no']
        page_size = 6
        limit = page_size * page_no
        query_value = "".join(
            [ch for ch in query_request['query'] if ch.isalpha() or ch == ' '])
        query_result = [
            cuisine for cuisine in await Recipe.find({
                'name': {
                    '$regex': f".*{query_value}.*",
                    '$options': 'i'
                }
            }).skip(limit - page_size).limit(page_size).to_list()
        ]
        query_result.append({
            "totalSize":
            await Recipe.find({
                'name': {
                    '$regex': f".*{query_value}.*",
                    '$options': 'i'
                }
            }).count()
        })
        return jsonify(query_result)
    return FALSE


@app.post("/api/predict")
async def predict_recipe():
    await init()
    data = request.get_json()
    query = data['queryString']
    if len(query) > 0:
        query = " ".join(query).lower()
        cuisine_list = [
            recipe.dict() for recipe in await Recipe.all().to_list()
        ]
        recipe = Recommender(cuisine_list, query)
        predicted_id = recipe.guide_predictor()
        recipe_data = await Recipe.find({
            "_id": {
                "$in": predicted_id
            }
        }).to_list()
        return jsonify(recipe_data)
    return FALSE


@app.post("/api/submit-query")
async def submit_query():
    await init()
    data = request.get_json()
    result = await UserQuery(data).save()
    return TRUE if result is not None else FALSE


@app.post("/api/userLikings")
async def user_likes():
    await init()
    user_data: Json = request.get_json()
    password = user_data["token"]
    if password:
        try:
            token = bytes(password, encoding="UTF-8")
            password = jwt.decode(token, "project", algorithms=["HS256"])
            result = await check_if_user_valid(user_data, password)
            if result and user_data['recipe_id'] is None:
                result_data = (await LikedRecipe.find_one(
                    LikedRecipe.user_id == result.id))
                result_data = result_data.dict() if result_data else {
                    'id': result.id,
                    'liked_recipes': []
                }
                if user_data['recommendation']:
                    result_data = await liked_response(result_data)
                    return result_data
                elif result_data:
                    return result_data
            return TRUE if await toggle_liked_recipes(user_data,
                                                      result) else FALSE
        except Exception as e:
            print(e)
            return FALSE
    return FALSE


async def toggle_liked_recipes(user_data, result):
    operation = '$push' if user_data['liked'] else '$pull'
    success = await LikedRecipe.find_one(
        {"user_id": result['id']},
        {operation: {
            'liked_recipe': user_data['recipe_id']
        }})
    if not success:
        success = await LikedRecipe.insert_one({
            "user_id":
            result['id'],
            "liked_recipe": [user_data['recipe_id']]
        })

    return success


async def check_if_user_valid(user_data, password):
    return await User.find_one({
        "user_name": user_data['user'],
        "password": password['password']
    })


async def liked_response(result_data: Dict[str, Any]) -> Dict[str, Any]:
    result: Dict[str, Any] = dict()
    cuisines = await Recipe.all().sort('id').to_list()
    liked = result_data["liked_recipes"]
    result_data["liked_recipes"] = [
        recipe for recipe in cuisines if recipe.id in liked
    ]
    result.update(result_data)
    result['recommendations'] = get_recommend(cuisines, liked)
    return result


if __name__ == "__main__":
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.run()
