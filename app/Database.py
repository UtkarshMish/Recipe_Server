import os
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models import Recipe, LikedRecipe, User, UserQuery


async def init():
    KEY = os.getenv("KEY")
    PASSWORD = os.getenv("PASSWORD")
    HOST = os.getenv("HOST")
    # Crete Motor client
    client = AsyncIOMotorClient(
        f"mongodb+srv://{KEY}:{PASSWORD}@{HOST}/test?retryWrites=true&w=majority"
    )

    # Init beanie with the Product document class
    await init_beanie(database=client.Recipe,
                      document_models=[User, UserQuery, LikedRecipe, Recipe])
