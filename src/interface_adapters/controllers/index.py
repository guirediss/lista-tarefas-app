from fastapi import APIRouter, HTTPException
from ...application.use_cases.index import TaskUseCases
from ...infrastructure.local_storage.memory import InMemoryTaskRepository
from ...domain.entities.index import Task

router = APIRouter()
task_repository = InMemoryTaskRepository()
task_use_cases = TaskUseCases(task_repository)

@router.post("/", response_model=Task)
async def create_task(task: Task):
    return task_use_cases.create_task(task.title, task.description)

@router.get("/", response_model=list[Task])
async def list_tasks():
    return task_use_cases.get_tasks()

@router.delete("/{task_id}", response_model=dict)
async def delete_task(task_id: int):
    success = task_use_cases.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}