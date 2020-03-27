from flask import Flask, json, jsonify,request
from flask_cors import CORS
from dotenv import load_dotenv, find_dotenv
import hashlib
import pymongo
import jwt
import os
app = Flask(__name__)
recipe_data = []
load_dotenv(find_dotenv())

KEY = os.getenv("KEY")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
client = pymongo.MongoClient(f'mongodb+srv://{KEY}:{PASSWORD}@{HOST}/test?retryWrites=true&w=majority')
db = client['Recipe']
user = db['Users']

with open("data.json", 'r') as data:
    recipe_data = json.load(data)

# Common Response
TRUE = {"value": True}
FALSE = {"value": False}
EXIST = {'value': 'exist'}



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = dict(request.get_json())

        if users['email']:
            users['email'] = str(users['email']).lower()
            users['password'] = hashlib.sha1(users['password'].encode()).hexdigest()
            result = user.find_one(users) or 0
            if result is not 0:
                encoded_jwt = jwt.encode({'password': users['password']}, 'project', algorithm='HS256').decode("UTF-8")
                return {"username": result['user_name'], "value": "true", "token": encoded_jwt}
            else:
                return FALSE
    return FALSE


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    print(request.environ['REMOTE_ADDR'])
    if request.method == 'POST':
        users = dict(request.get_json())
        users['user_name'] = users['user_name'].capitalize()
        if users['email']:
            users['email'] = str(users['email']).lower()
            users['password'] = hashlib.sha1(users['password'].encode()).hexdigest()
            result = user.find_one({'email': users['email']}) or 0
            if result is not 0:
                return EXIST
            else:
                encoded_jwt = jwt.encode({'password': users['password']}, 'project', algorithm='HS256').decode("UTF-8")
                user.insert_one(users)
                return {"username": users['user_name'], "value": "success", "token": encoded_jwt}
    return FALSE


@app.route('/api/verify-token', methods=['GET', 'POST'])
def check_api():
    if request.method == 'POST':
        user_data = request.get_json()
        token = user_data['token']
        if not token:
            return FALSE
        else:
            token = bytes(token, encoding="UTF-8")
            try:
                password = jwt.decode(token, "project", algorithms=['HS256'])
            except:
                return FALSE
            result = user.find_one(password) or 0
            if result is not 0:
                return TRUE
            else:
                return FALSE
    return FALSE


@app.route('/api/get-recipe/<int:pageno>', methods=['GET', 'POST'])
def get_cuisine(pageno=None):
    pageno = int(pageno)
    if pageno > 0:
        limit = 21*pageno
        recipe = recipe_data[(limit-21):limit]
        recipe.append({"totalSize": len(recipe_data)})
        return jsonify(recipe)
    return TRUE


if __name__ == '__main__':
    app.run(debug=True)
    CORS(app, resources={r'/*': {'origins': '*'}})
