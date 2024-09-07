from fastapi.applications import FastAPI

from task_management.api.routers import register_routers
from task_management.util.tools import pipe


def create_instance() -> FastAPI:
    return FastAPI()


def init_app() -> FastAPI:
    app: FastAPI = pipe(
        create_instance(),
        register_routers
    )
    return app
