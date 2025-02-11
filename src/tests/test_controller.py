import sys
import os
import pytest
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.main.main import app
from src.infrastructure.local_storage.memory import InMemoryTaskRepository
from src.interface_adapters.controllers.index import task_repository

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_repository():
    task_repository.tasks.clear()
    task_repository.current_id = 1

def test_list_tasks_empty(clear_repository):
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_task():
    response = client.post("/tasks/", json={"title": "Test Task", "description": "This is a test task"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
    assert response.json()["description"] == "This is a test task"

def test_create_task_without_title():
    response = client.post("/tasks/", json={"description": "This task has no title"})
    assert response.status_code == 422

def test_list_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_task():
    create_response = client.post("/tasks/", json={"title": "Task to Delete", "description": "This task will be deleted"})
    assert create_response.status_code == 200
    task_id = create_response.json()["id"]

    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Task deleted successfully"

    list_response = client.get("/tasks/")
    tasks = list_response.json()
    assert all(task["id"] != task_id for task in tasks)

def test_delete_nonexistent_task():
    response = client.delete("/tasks/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"