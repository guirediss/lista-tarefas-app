from typing import List
from ...domain.entities.index import Task
from ...domain.repositories.index import TaskRepository

class TaskUseCases:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def create_task(self, title: str, description: str) -> Task:
        task = Task(
            id=self.task_repository.get_next_id(),
            title=title,
            description=description,
            completed=False
        )
        self.task_repository.add_task(task)
        return task

    def get_tasks(self) -> List[Task]:
        return self.task_repository.get_all_tasks()

    def delete_task(self, task_id: int) -> bool:
        return self.task_repository.remove_task(task_id)

    def format_task(self, task: Task) -> dict:
        return {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "completed": task.completed
        }

    def format_tasks(self, tasks: List[Task]) -> List[dict]:
        return [self.format_task(task) for task in tasks]