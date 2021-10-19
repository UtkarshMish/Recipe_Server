import hashlib
from pymongo import ReturnDocument
from typing import Any, Dict, List, Optional
from Recipe_Model import Recommender
from app.models import LikedRecipe, Recipe, User
import jwt

from app.models.query import LikedQuery
# Common Response
TRUE = {"value": True}
FALSE = {"value": False}
EXIST = {"value": "exist"}


async def check_if_user_valid(user_name: str, password: str):
    return await User.find_one({"user_name": user_name, "password": password})


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


async def toggle_liked_recipes(user_data: LikedQuery, user: User) -> bool:
    operation = '$push' if user_data.liked else '$pull'
    user_likings = await LikedRecipe.find_one(LikedRecipe.user_id == user.id)
    try:
        if user_likings:
            await LikedRecipe.find_one({
                "user_id": user.id
            }).update({operation: {
                'liked_recipe': user_data.recipe_id
            }})
        else:
            await LikedRecipe(user_id=user.id,
                              liked_recipes=[user_data.recipe_id]).insert()
    except Exception as e:
        print(e)
        return False

    return True


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


def get_token(password: str):
    encoded_jwt = jwt.encode({"password": password},
                             "project",
                             algorithm="HS256")

    return encoded_jwt


def get_recommend(cuisines: List[Recipe], result_data: Optional[Dict[str,
                                                                     Any]]):
    recommender = Recommender([cusine.dict() for cusine in cuisines],
                              result_data)
    return recommender.user_like_recommend()


def get_password(token: str):
    password: str = jwt.decode(token, "project",
                               algorithms=["HS256"])["password"]
    password = hashlib.sha1(password.encode()).hexdigest()
    return password
