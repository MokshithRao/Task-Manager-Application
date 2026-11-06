from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import Task


app = FastAPI()

# Load HTML templates from the templates folder.
templates = Jinja2Templates(directory="templates")


# Serve CSS and images from the static folder.
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# Create database tables for registered ORM models.
Base.metadata.create_all(bind=engine)



@app.get("/")
def home():
    return {"message": "Welcome to Task Manager"}


@app.get("/tasks")
def show_tasks(request: Request, db: Session = Depends(get_db)):

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