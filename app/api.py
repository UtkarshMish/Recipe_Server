import hashlib
from typing import Optional

from fastapi import APIRouter
from Recipe_Model import Recommender

from app.models import (LikedRecipe, Recipe, User, UserField, UserModel,
                        UserQuery, UserQueryModel)
from app.models.query import LikedQuery, PageSearch, QueryJson, Token
from app.utils import (EXIST, FALSE, TRUE, check_if_user_valid, get_password,
                       get_token, liked_response, toggle_liked_recipes)

apiRoute = APIRouter(prefix="/api")


@apiRoute.post("/login")
async def login(user: UserModel):
    result = await User.find_one(User.email == user.email)
    if result and result.password == hashlib.sha1(
            user.password.encode()).hexdigest():
        encoded_jwt = get_token(user.password)
        return {
            "username": result.user_name,
            "value": "true",
            "token": encoded_jwt,
        }
    return FALSE


@apiRoute.post("/signup")
async def signup(newUser: UserField):

    newUser.user_name = newUser.user_name.capitalize()
    if newUser.email:
        newUser.email = str(newUser.email).lower()
        newUser.password = hashlib.sha1(newUser.password.encode()).hexdigest()
        result = await User.find_one(User.email == newUser.email)
        if result:
            return EXIST
        else:
            encoded_jwt = get_token(newUser.password)
            try:
                await User(user_name=newUser.user_name,
                           email=newUser.email,
                           password=newUser.password).create()
                return {
                    "username": newUser.user_name,
                    "value": "success",
                    "token": encoded_jwt,
                }
            except Exception:
                return {"username": newUser.user_name, "value": "failed"}
    return FALSE


@apiRoute.post("/verify-token")
async def check_api(user_data: Token):

    token = user_data.token
    if not token:
        return FALSE
    else:
        try:
            password = get_password(token)
            result = await User.find_one(User.password == password)
            return TRUE if result else FALSE
        except Exception:
            return FALSE


@apiRoute.get("/get-recipe/")
@apiRoute.get("/get-recipe/{page_no}")
async def get_cuisine(page_no: Optional[int] = 1):
    if page_no > 0:
        page_size = 6
        limit = page_size * page_no
        recipe_data = [
            recipe.dict()
            for recipe in await Recipe.all(projection_model=Recipe).skip(
                limit - page_size).limit(page_size).to_list()
        ]

        recipe_data.append({"totalSize": await Recipe.count() + 1})
        return recipe_data
    return FALSE


@apiRoute.get("/recipe/{recipe_id:str}")
async def get_recipe(recipe_id: str):

    recipe_data = await Recipe.get(recipe_id)
    return recipe_data.dict() if recipe_data else FALSE


@apiRoute.post("/search")
async def search(user_query: PageSearch):

    if user_query:
        page_no = user_query.page_no
        page_size = 6
        limit = page_size * page_no
        query_value = user_query.query if user_query.query.isalpha() else ""

        recipe_query = Recipe.find_many(Recipe.name == {
            '$regex': f".*{query_value}.*",
            '$options': 'i'
        })
        recipe_response = [
            cuisine for cuisine in await recipe_query.skip(
                limit - page_size).limit(page_size).to_list()
        ]
        recipe_response.append({"totalSize": await recipe_query.count()})
        return recipe_response
    return FALSE


@apiRoute.post("/predict")
async def predict_recipe(data: QueryJson):

    query = data.queryString
    if len(query) > 0:
        query = " ".join(query).lower()
        cuisine_list = [
            recipe.dict() for recipe in await Recipe.all().to_list()
        ]
        recipe = Recommender(cuisine_list, query)
        predicted_id = recipe.guide_predictor()
        recipe_data = [
            recipe.dict() for recipe in await Recipe.find({
                "_id": {
                    "$in": predicted_id
                }
            }).to_list()
        ]
        return recipe_data
    return FALSE


@apiRoute.post("/submit-query")
async def submit_query(data: UserQueryModel):

    result = await UserQuery(data).save()
    return TRUE if result is not None else FALSE


@apiRoute.post("/userLikings")
async def user_likes(user_data: LikedQuery):
    if user_data.token:
        try:
            password = get_password(user_data.token)
            result = await check_if_user_valid(user_data.user, password)
            if result and user_data.recipe_id is None:
                result_data = (await LikedRecipe.find_one(
                    LikedRecipe.user_id == result.id))
                result_data = result_data.dict() if result_data else {
                    'id': result.id,
                    'liked_recipes': []
                }
                if user_data.recommendation:
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
