import sys
from typing import List

from src.repository.in_memory import InMemoryTaskRepository
from src.service.task_service import TaskService


def format_list(tasks) -> List[str]:
    lines = []
    for i, t in enumerate(tasks, start=1):
        mark = "[x]" if t.completed else "[ ]"
        lines.append(f"{i}. {mark} {t.description}")
    return lines


def usage() -> str:
    return (
        "Usage:\n"
        "  add \"<description>\"\n"
        "  list\n"
        "  done <number>\n"
    )


_REPO = InMemoryTaskRepository()
_SERVICE = TaskService(_REPO)


def main(argv: List[str]) -> int:

    if not argv:
        print(usage())
        return 1

    cmd = argv[0]
    try:
        if cmd == "add":
            if len(argv) < 2:
                print("Error: description required\n" + usage())
                return 1
            desc = argv[1]
            _SERVICE.add_task(desc)
            return 0
        elif cmd == "list":
            tasks = _SERVICE.list_tasks()
            for line in format_list(tasks):
                print(line)
            return 0
        elif cmd == "done":
            if len(argv) < 2:
                print("Error: task number required\n" + usage())
                return 1
            try:
                index = int(argv[1])
            except ValueError:
                print("Error: task number must be an integer")
                return 1
            _SERVICE.complete_task_by_index(index)
            return 0
        else:
            print("Error: unknown command\n" + usage())
            return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
