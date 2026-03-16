# task_utils.py
tasks = []  # List to store all tasks

# Example task structure
task_example = {
    "title": "Groceries",
    "description": "Shop at Market Basket for food",
    "due_date": "2024-06-26",
    "completed": False
}

# task_utils.py
from task_manager import validation

tasks = []

def add_task(title, description, due_date):
    title = validation.validate_task_title(title)
    description = validation.validate_task_description(description)
    due_date = validation.validate_due_date(due_date)

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print(f"Task '{title}' added successfully!")

def mark_task_as_complete(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"Task '{tasks[task_index]['title']}' marked as complete.")
    else:
        print("Invalid task index.")

def view_pending_tasks():
    print("\nPending Tasks:")
    for idx, task in enumerate(tasks):
        if not task["completed"]:
            print(f"{idx}. {task['title']} - Due: {task['due_date']}")

def calculate_progress():
    if not tasks:
        return 0
    completed_tasks = sum(1 for task in tasks if task["completed"])
    progress = (completed_tasks / len(tasks)) * 100
    return round(progress, 2)