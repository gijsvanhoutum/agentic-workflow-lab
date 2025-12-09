import pytest

from src.repository.in_memory import InMemoryTaskRepository
from src.service.task_service import TaskService


def test_add_task_validates_description():
    service = TaskService(InMemoryTaskRepository())
    with pytest.raises(ValueError):
        service.add_task("")
    with pytest.raises(ValueError):
        service.add_task("   ")


def test_add_task_success():
    service = TaskService(InMemoryTaskRepository())
    t = service.add_task("Hello")
    assert t.description == "Hello" and t.completed is False


def test_complete_task_index_validation():
    service = TaskService(InMemoryTaskRepository())
    with pytest.raises(ValueError):
        service.complete_task_by_index(0)
    with pytest.raises(ValueError):
        service.complete_task_by_index(-1)
    with pytest.raises(ValueError):
        service.complete_task_by_index("a")  # type: ignore


def test_complete_task_success_flow():
    repo = InMemoryTaskRepository()
    service = TaskService(repo)
    service.add_task("A")
    updated = service.complete_task_by_index(1)
    assert updated.completed is True
    assert repo.list()[0].completed is True
