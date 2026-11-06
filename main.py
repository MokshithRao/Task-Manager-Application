from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database import engine, SessionLocal, Base
from database import engine, Base
from models import Task


app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)



Base.metadata.create_all(bind=engine)



@app.get("/")
def home():
    return {"message": "Welcome to Task Manager"}

@app.get("/tasks")
def show_tasks(request: Request):

    tasks = [
        {
            "title": "Learn FastAPI",
            "completed": True
        },
        {
            "title": "Complete SQL assignment",
            "completed": False
        },
        {
            "title": "Build Task Manager",
            "completed": False
        }
    ]

    return templates.TemplateResponse(
        request = request,
        name = "tasks.html",
        context = {
            "tasks": tasks
        }
    )