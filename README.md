# Task Manager Web Application

A simple Task Manager web application built using **Python, FastAPI, Jinja2, SQLAlchemy, and SQLite**. It allows users to create, view, update, complete, and delete tasks through a clean, server-rendered web interface.

## Features

- **Create Tasks:** Add new tasks using the input form.
- **View Tasks:** Display all tasks stored in the database.
- **Update Tasks:** Edit the title of an existing task.
- **Complete Tasks:** Mark pending tasks as completed.
- **Delete Tasks:** Remove tasks from the database.
- **Task Statistics:** View total, completed, and pending task counts.
- **Persistent Storage:** Store tasks in an SQLite database using SQLAlchemy ORM.
- **Responsive UI:** Access the application through desktop and mobile browsers.

## Technologies Used

- **Backend:** Python, FastAPI
- **Frontend:** HTML, CSS, Jinja2
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Server:** Uvicorn

## Project Structure

```text
task-Manager-Application/
│
├── main.py
├── database.py
├── models.py
├── task_manager.db
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── tasks.html
│
└── static/
    ├── css/
    │   └── style.css
    └── images/
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/MokshithRao/Task-Manager-Application.git
cd Task-Manager-Application
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
uvicorn main:app --reload
```

### 6. Open the application

Visit the following address in your browser:

```text
http://127.0.0.1:8000/tasks
```

## Database

The application uses SQLite for data storage and SQLAlchemy ORM for database operations.

The database and required tables are created automatically when the application starts.

## Learning Outcomes

Through this project, I gained practical experience with:

- Building backend applications using FastAPI.
- Rendering dynamic HTML pages using Jinja2.
- Serving static files using FastAPI.
- Connecting applications to databases using SQLAlchemy ORM.
- Implementing CRUD operations.
- Managing database sessions and application requests.
- Working with Git and GitHub for version control.