from typing import List
from src.domain.entities.index import Task

def format_task(task: Task) -> dict:
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }

def format_tasks(tasks: List[Task]) -> List[dict]:
    return [format_task(task) for task in tasks]