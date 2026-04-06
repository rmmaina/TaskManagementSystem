# main.py

from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)

def main():
    tasks = []

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            description = input("Enter description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, title, description, due_date)

        elif choice == "2":
            if len(tasks) == 0:
                print("No tasks available.")
                continue

            print("\nAll Tasks:")
            for i, task in enumerate(tasks):
                status = "✔" if task["completed"] else "✘"
                print(f"{i + 1}. {task['title']} [{status}]")

            try:
                index = int(input("Enter task number to mark complete: ")) - 1
                mark_task_as_complete(tasks, index)
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "3":
            view_pending_tasks(tasks)

        elif choice == "4":
            calculate_progress(tasks)

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()