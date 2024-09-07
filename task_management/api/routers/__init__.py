from fastapi.applications import FastAPI

from task_management.api.routers import health, task


def register_routers(app: FastAPI) -> FastAPI:
    app.include_router(health.router)
    app.include_router(task.router)
    return app
