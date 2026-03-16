# validation.py
import datetime

def validate_task_title(title):
    if not title or len(title.strip()) == 0:
        raise ValueError("Title cannot be empty.")
    return title.strip()

def validate_task_description(description):
    if not description or len(description.strip()) == 0:
        raise ValueError("Description cannot be empty.")
    return description.strip()

def validate_due_date(due_date):
    try:
        datetime.datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")
    return due_date