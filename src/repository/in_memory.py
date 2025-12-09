from typing import List
from datetime import datetime

from src.models.task import Task
from src.repository.interface import ITaskRepository

class InMemoryTaskRepository(ITaskRepository):
    def __init__(self) -> None:
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add(self, description: str) -> Task:
        task = Task(id=self._next_id, description=description, completed=False, created_at=datetime.utcnow())
        self._tasks.append(task)
        self._next_id += 1
        return task

    def list(self) -> List[Task]:
        return list(self._tasks)

    def complete_by_index(self, index_1_based: int) -> Task:
        idx = index_1_based - 1
        if idx < 0 or idx >= len(self._tasks):
            raise IndexError("Task index out of range")
        task = self._tasks[idx]
        if task.completed:
            raise ValueError("Task already completed")
        updated = Task(id=task.id, description=task.description, completed=True, created_at=task.created_at)
        self._tasks[idx] = updated
        return updated
