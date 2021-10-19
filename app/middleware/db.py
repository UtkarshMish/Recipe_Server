from fastapi import FastAPI, Request
from app.database import init


class ConnectToDB():
    def __init__(self, app: FastAPI) -> None:
        app.middleware("http")(ConnectToDB.initialize_database)

    @staticmethod
    async def initialize_database(request: Request, call_next):
        await init()
        response = await call_next(request)
        return response
