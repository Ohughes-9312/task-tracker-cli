# -------------------------
# 1. IMPORTS
# -------------------------
import json
import os
from datetime import datetime

# -------------------------
# 2. CONSTANTS
# -------------------------
TASKS_FILE = "tasks.json"

# -------------------------
# 3. HELPER FUNCTIONS
# -------------------------
def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []

    with open(TASKS_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def get_next_id(tasks):
    """Generate a persistent incremental ID."""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


# -------------------------
# 4. CORE TASK OPERATIONS
# -------------------------
def add_task(description):
    """Add a new task to the list."""
    tasks = load_tasks()

    new_task = {
        "id": get_next_id(tasks),
        "description": description,
        "completed": False,
        "created_at": datetime.now().isoformat(),
        "completed_at": None
    }

    tasks.append(new_task)
    save_tasks(tasks)
    return new_task


def list_tasks():
    """Return all tasks."""
    return load_tasks()


def complete_task(task_id):
    """Mark a task as completed."""
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            task["completed_at"] = datetime.now().isoformat()
            save_tasks(tasks)
            return task

    return None


def delete_task(task_id):
    """Delete a task by ID."""
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]

    if len(updated_tasks) == len(tasks):
        return False  # No task was deleted

    save_tasks(updated_tasks)
    return True