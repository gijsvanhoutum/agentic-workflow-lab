from __future__ import annotations
from typing import List
from datetime import datetime
from pathlib import Path
import json

from src.models.task import Task
from src.repository.interface import ITaskRepository


class FileTaskRepository(ITaskRepository):
    def __init__(self, file_path: Path) -> None:
        self._file_path = Path(file_path)
        self._tasks: List[Task] = []
        self._next_id: int = 1
        self._load()

    def _load(self) -> None:
        if not self._file_path.exists():
            self._file_path.parent.mkdir(parents=True, exist_ok=True)
            self._save()  # initialize empty file
            return
        try:
            raw = json.loads(self._file_path.read_text())
            self._tasks = [
                Task(
                    id=int(t.get("id")),
                    description=str(t.get("description")),
                    completed=bool(t.get("completed")),
                    created_at=datetime.fromisoformat(t.get("created_at")),
                )
                for t in raw.get("tasks", [])
            ]
            self._next_id = int(
                raw.get("next_id", (max((x.id for x in self._tasks), default=0) + 1)))
        except Exception:
            # If the file is corrupt, start fresh
            self._tasks = []
            self._next_id = 1

    def _save(self) -> None:
        payload = {
            "next_id": self._next_id,
            "tasks": [
                {
                    "id": t.id,
                    "description": t.description,
                    "completed": t.completed,
                    "created_at": t.created_at.isoformat(),
                }
                for t in self._tasks
            ],
        }
        self._file_path.write_text(json.dumps(payload, indent=2))

    def add(self, description: str) -> Task:
        task = Task(id=self._next_id, description=description,
                    completed=False, created_at=datetime.utcnow())
        self._tasks.append(task)
        self._next_id += 1
        self._save()
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
        updated = Task(id=task.id, description=task.description,
                       completed=True, created_at=task.created_at)
        self._tasks[idx] = updated
        self._save()
        return updated
