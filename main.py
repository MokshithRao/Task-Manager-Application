from fastapi import FastAPI, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
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

    tasks = db.query(Task).order_by(Task.id.desc()).all()


    return templates.TemplateResponse(
        request = request,
        name = "tasks.html",
        context = {
            "tasks": tasks
        }
    )


@app.post("/tasks")
def create_task(title: str = Form(...), db: Session = Depends(get_db)):
    new_task = Task(title=title)

    db.add(new_task)
    db.commit()

    return RedirectResponse(url="/tasks", status_code=303)