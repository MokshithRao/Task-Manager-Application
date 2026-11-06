from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home():
    return {"message": "Welcome to Task Manager"}

@app.get("/tasks")
def show_tasks(request: Request):

    return templates.TemplateResponse(
        request = request,
        name = "tasks.html",
        context = {
            "title": "My Task Manager",
            "message": "Welcome! Start managing your tasks"
        }
    )