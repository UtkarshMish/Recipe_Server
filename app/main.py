from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
from app.middleware import ConnectToDB
from app.api import apiRoute
from app.routes import homeRoute
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

load_dotenv(find_dotenv())


def create_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(CORSMiddleware,
                       allow_origins=["*"],
                       allow_credentials=True,
                       allow_methods=["*"],
                       allow_headers=["*"])
    app.mount("/static", StaticFiles(directory="./app/static"), name="static")

    ConnectToDB(app)
    app.include_router(apiRoute)
    app.include_router(homeRoute)
    return app
