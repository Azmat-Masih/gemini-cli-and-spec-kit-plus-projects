from src.app.services import add_task, get_tasks, update_task, delete_task, toggle_complete, get_task_by_id
from src.app.utils import get_string_input, get_integer_input, confirm_action, print_tasks

def main():
    while True:
        print("\n--- Todo App Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Toggle Complete")
        print("0. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            title = get_string_input("Enter task title (1-200 chars): ", min_length=1, max_length=200, optional=False)
            if title:
                description = get_string_input("Enter task description (optional, max 1000 chars): ", max_length=1000, optional=True)
                try:
                    task = add_task(title, description if description else None)
                    print(f"Task added: {task.title} (ID: {task.id})")
                except ValueError as e:
                    print(f"Error adding task: {e}")
        elif choice == '2':
            tasks = get_tasks()
            print_tasks(tasks)
        elif choice == '3':
            task_id = get_integer_input("Enter the ID of the task to update: ")
            if task_id is not None:
                task_to_update = get_task_by_id(task_id)
                if task_to_update:
                    print(f"Current Task: ID: {task_to_update.id}, Title: {task_to_update.title}, Desc: {task_to_update.description}")
                    new_title = get_string_input("Enter new title (leave blank to keep current): ", min_length=1, max_length=200, optional=True)
                    new_description = get_string_input("Enter new description (leave blank to keep current): ", max_length=1000, optional=True)
                    
                    if new_title is not None or new_description is not None:
                        updated_task = update_task(task_id, new_title if new_title != "" else None, new_description if new_description != "" else None)
                        if updated_task:
                            print(f"Task {task_id} updated.")
                        else:
                            print(f"Failed to update task {task_id}.") # Should not happen if get_task_by_id worked
                    else:
                        print("No changes specified.")
                else:
                    print(f"Task with ID {task_id} not found.")
        elif choice == '4':
            task_id = get_integer_input("Enter the ID of the task to delete: ")
            if task_id is not None:
                if get_task_by_id(task_id): # Check if task exists before asking for confirmation
                    if confirm_action(f"Are you sure you want to delete task {task_id}?"):
                        if delete_task(task_id):
                            print(f"Task {task_id} deleted.")
                        else:
                            print(f"Failed to delete task {task_id}.")
                else:
                    print(f"Task with ID {task_id} not found.")
        elif choice == '5':
            task_id = get_integer_input("Enter the ID of the task to toggle completion: ")
            if task_id is not None:
                toggled_task = toggle_complete(task_id)
                if toggled_task:
                    status = "completed" if toggled_task.completed else "incomplete"
                    print(f"Task {task_id} marked as {status}.")
                else:
                    print(f"Task with ID {task_id} not found.")
        elif choice == '0':
            print("Exiting Todo App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
