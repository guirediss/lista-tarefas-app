from fastapi import FastAPI
from ..interface_adapters.controllers.index import router as task_router

app = FastAPI()

app.include_router(task_router, prefix="/tasks", tags=["tasks"])