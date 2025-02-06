from ...domain.entities.index import Task
from ...domain.repositories.index import TaskRepository
from typing import List

class InMemoryTaskRepository(TaskRepository):
    def __init__(self):
        self.tasks = {}
        self.current_id = 1

    def add_task(self, task: Task) -> None:
        self.tasks[self.current_id] = task
        self.current_id += 1

    def get_all_tasks(self) -> List[Task]:
        return list(self.tasks.values())

    def remove_task(self, task_id: int) -> bool:
        return self.tasks.pop(task_id, None) is not None

    def get_next_id(self) -> int:
        return self.current_id