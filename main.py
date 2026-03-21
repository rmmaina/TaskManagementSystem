from task_manager.task_utils import add_task
import task_manager.task_utils as task_utils

try:
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date: ")

    msg = add_task(title, description, due_date)
    print(msg)

except ValueError as e:
    print(f"Error: {e}")

tasks = task_utils.view_pending_tasks()
print("\nPending Tasks:")
for task in tasks:
    print(task)

index = int(input("Enter task index to mark complete: "))
msg = task_utils.mark_task_as_complete(index)
print(msg)
