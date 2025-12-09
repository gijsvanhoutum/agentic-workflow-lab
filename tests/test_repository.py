import pytest

from src.repository.in_memory import InMemoryTaskRepository


def test_add_and_list_order():
    repo = InMemoryTaskRepository()
    repo.add("Task A")
    repo.add("Task B")
    tasks = repo.list()
    assert [t.description for t in tasks] == ["Task A", "Task B"]
    assert tasks[0].id == 1 and tasks[1].id == 2


def test_list_returns_copy():
    repo = InMemoryTaskRepository()
    repo.add("T1")
    tasks1 = repo.list()
    tasks2 = repo.list()
    assert tasks1 is not tasks2


def test_complete_by_valid_index():
    repo = InMemoryTaskRepository()
    repo.add("T1")
    updated = repo.complete_by_index(1)
    assert updated.completed is True
    assert repo.list()[0].completed is True


def test_complete_by_invalid_index_raises():
    repo = InMemoryTaskRepository()
    repo.add("T1")
    with pytest.raises(IndexError):
        repo.complete_by_index(2)


def test_complete_already_completed_raises():
    repo = InMemoryTaskRepository()
    repo.add("T1")
    repo.complete_by_index(1)
    with pytest.raises(ValueError):
        repo.complete_by_index(1)
