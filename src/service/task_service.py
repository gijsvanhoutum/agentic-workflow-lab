from typing import List

from src.models.task import Task
from src.repository.interface import ITaskRepository

class TaskService:
    def __init__(self, repo: ITaskRepository) -> None:
        self._repo = repo

    def add_task(self, description: str) -> Task:
        desc = (description or "").strip()
        if not desc:
            raise ValueError("Description must not be empty")
        return self._repo.add(desc)

    def list_tasks(self) -> List[Task]:
        return self._repo.list()

    def complete_task_by_index(self, index_1_based: int) -> Task:
        if not isinstance(index_1_based, int):
            raise ValueError("Index must be an integer")
        if index_1_based <= 0:
            raise ValueError("Index must be a positive integer")
        return self._repo.complete_by_index(index_1_based)
