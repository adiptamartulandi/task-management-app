from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from typing import Literal

from task_management.core.task_app import TaskManagementApp
from task_management.config import ES_CONFIG


router = APIRouter()
task_app = TaskManagementApp(ES_CONFIG)


@router.post("/tasks")
async def create(title: str, description: str, status: str = "todo"):
    task_app.create_task(title, description, status)
    return JSONResponse(dict(status="Task created successfully."), status_code=201)


@router.get("/tasks/{title}")
async def get_task(title: str):
    task = task_app.read_task(title)
    if task:
        return JSONResponse(dict(task=task), status_code=200)
    else:
        return JSONResponse(dict(error="Task not found, please check the title."), status_code=404)


@router.put("/tasks/{title}")
async def update(title: str, type: Literal['description', 'status'], value: str):
    message = task_app.update_task(title, type, value)
    if message:
        return JSONResponse(dict(error=message), status_code=400)
    else:
        return JSONResponse(dict(status="Task updated successfully."), status_code=200)


@router.delete("/tasks/{title}")
async def delete(title: str):
    message = task_app.delete_task(title)
    if message:
        return JSONResponse(dict(error=message), status_code=404)
    else:
        return JSONResponse(dict(status="Task deleted successfully."), status_code=200)


@router.get("/tasks")
async def get_all_tasks():
    tasks = task_app.show_all_tasks()
    return JSONResponse(dict(tasks=tasks), status_code=200)
