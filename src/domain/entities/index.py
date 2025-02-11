from pydantic import BaseModel

class Task(BaseModel):
    id: int | None = None
    title: str
    description: str
    completed: bool = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed})"