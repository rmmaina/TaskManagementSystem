# task_manager/task_utils.py

from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

def add_task(tasks, title, description, due_date):
    if not validate_task_title(title):
        return
    if not validate_task_description(description):
        return
    if not validate_due_date(due_date):
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(tasks, index):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    if index < 0 or index >= len(tasks):
        print("Error: Invalid task number.")
        return

    tasks[index]["completed"] = True
    print("Task marked as complete!")


def view_pending_tasks(tasks):
    pending = [task for task in tasks if not task["completed"]]

    if len(pending) == 0:
        print("No pending tasks.")
        return

    print("\nPending Tasks:")
    for i, task in enumerate(pending):
        print(f"{i + 1}. {task['title']} - Due: {task['due_date']}")


def calculate_progress(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    completed = sum(1 for task in tasks if task["completed"])
    total = len(tasks)

    progress = (completed / total) * 100
    print(f"Progress: {progress:.2f}% ({completed}/{total} tasks completed)")