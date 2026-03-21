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
    return f"Task '{title}' added successfully!"


def mark_task_as_complete(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        return f"Task '{tasks[task_index]['title']}' marked as complete."
    return "Invalid task index."


def view_pending_tasks():
    return [
        f"{idx}. {task['title']} - Due: {task['due_date']}"
        for idx, task in enumerate(tasks)
        if not task["completed"]
    ]