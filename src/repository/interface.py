from typing import List
from abc import ABC, abstractmethod

from src.models.task import Task

class ITaskRepository(ABC):
    @abstractmethod
    def add(self, description: str) -> Task:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[Task]:
        raise NotImplementedError

    @abstractmethod
    def complete_by_index(self, index_1_based: int) -> Task:
        raise NotImplementedError
