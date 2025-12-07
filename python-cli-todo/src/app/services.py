from typing import List, Optional
from src.app.models import Task

_tasks: List[Task] = []
_next_id = 1

def _get_next_id() -> int:
    global _next_id
    current_id = _next_id
    _next_id += 1
    return current_id

def _find_task_index(task_id: int) -> Optional[int]:
    for i, task in enumerate(_tasks):
        if task.id == task_id:
            return i
    return None

def add_task(title: str, description: Optional[str] = None) -> Task:
    task = Task(title=title, description=description)
    _tasks.append(task)
    return task

def get_tasks() -> List[Task]:
    return _tasks

def update_task(task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
    index = _find_task_index(task_id)
    if index is None:
        return None
    
    task = _tasks[index]
    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    return task

def delete_task(task_id: int) -> bool:
    index = _find_task_index(task_id)
    if index is None:
        return False
    del _tasks[index]
    return True

def toggle_complete(task_id: int) -> Optional[Task]:
    index = _find_task_index(task_id)
    if index is None:
        return None
    task = _tasks[index]
    task.completed = not task.completed
    return task

def get_task_by_id(task_id: int) -> Optional[Task]:
    index = _find_task_index(task_id)
    if index is None:
        return None
    return _tasks[index]

def reset_tasks():
    """Resets the in-memory task list and ID counter for testing."""
    global _tasks, _next_id
    _tasks = []
    _next_id = 1
    Task._next_id = 1 # Also reset the model's internal counter
