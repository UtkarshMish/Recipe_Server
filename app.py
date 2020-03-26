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
client = pymongo.MongoClient(f'mongodb+srv://{KEY}:{PASSWORD}@recipe-mipii.mongodb.net/test?retryWrites=true&w=majority')
db = client['Recipe']
user = db['Users']

with open("data.json", 'r') as data:
    recipe_data = json.load(data)

# Common Response
TRUE = {"value": True}
FALSE = {"value": False}
EXIST = {'value': 'exist'}


@app.route('/', methods=['GET', 'POST'])
def get_recipe(limit=0):
    if request.method == 'POST':
        limit = int(request.data) or limit
        response_data = recipe_data[:limit]

        return jsonify(response_data)
    else:
        return "invalid request"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = dict(request.get_json())
        if users['email']:
            users['email'] = str(users['email']).lower()
            users['password'] = hashlib.sha1(users['password'].encode()).hexdigest()
            result = user.find({'email': users['email'], 'password': users['password']}) or False
            if result.count() is not 0:
                for record in result:
                    encoded_jwt = jwt.encode({'password': users['password']}, 'project', algorithm='HS256').decode("UTF-8")
                    return {"username": record['user_name'], "value": "true", "token": encoded_jwt}
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
            if db['Users'].find({'email': users['email']}).count() > 0:
                return EXIST
            else:
                encoded_jwt = jwt.encode({'password': users['password']}, 'project', algorithm='HS256').decode("UTF-8")
                db['Users'].insert_one(users)
                return {"username": users['user_name'], "value": "success", "token": encoded_jwt}
        else:
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
            password = jwt.decode(jwt=token, key='project', algorithms=['HS256'])
            if db['Users'].find(password).count() > 0:
                return TRUE
            else:
                return FALSE
    return FALSE


if __name__ == '__main__':
    app.run(debug=True)
    CORS(app, resources={r'/*': {'origins': '*'}})
