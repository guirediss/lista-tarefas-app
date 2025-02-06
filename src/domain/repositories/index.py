from abc import ABC, abstractmethod
from typing import List
from ..entities.index import Task

class TaskRepository(ABC):
    @abstractmethod
    def add_task(self, task: Task) -> None:
        pass

    @abstractmethod
    def get_all_tasks(self) -> List[Task]:
        pass

    @abstractmethod
    def remove_task(self, task_id: int) -> None:
        pass