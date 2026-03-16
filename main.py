# main.py
from task_manager import task_utils

def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. View Pending Tasks")
        print("3. Mark Task as Complete")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                task_utils.add_task(title, description, due_date)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            task_utils.view_pending_tasks()

        elif choice == "3":
            task_utils.view_pending_tasks()
            index = int(input("Enter task index to mark complete: "))
            task_utils.mark_task_as_complete(index)

        elif choice == "4":
            progress = task_utils.calculate_progress()
            print(f"Task completion progress: {progress}%")

        elif choice == "5":
            print("Exiting Task Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()