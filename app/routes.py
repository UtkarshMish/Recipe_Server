from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

homeRoute = APIRouter()

templates = Jinja2Templates("./app/templates")


@homeRoute.get("/{_:path}", response_class=HTMLResponse)
def recipe_advisor(request: Request, _: str):
    return templates.TemplateResponse("index.html", {"request": request})
