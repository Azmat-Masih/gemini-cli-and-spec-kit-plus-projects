from typing import Optional

def get_string_input(prompt: str, min_length: int = 1, max_length: int = 200, optional: bool = False) -> Optional[str]:
    while True:
        user_input = input(prompt).strip()
        if optional and not user_input:
            return None
        if not user_input:
            print("Input cannot be empty. Please try again.")
        elif not (min_length <= len(user_input) <= max_length):
            print(f"Input must be between {min_length} and {max_length} characters. Please try again.")
        else:
            return user_input

def get_integer_input(prompt: str) -> Optional[int]:
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Input cannot be empty. Please try again.")
        else:
            try:
                return int(user_input)
            except ValueError:
                print("Invalid input. Please enter a number.")

def confirm_action(prompt: str) -> bool:
    while True:
        user_input = input(f"{prompt} (yes/no): ").strip().lower()
        if user_input in ["yes", "y"]:
            return True
        elif user_input in ["no", "n"]:
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

def print_tasks(tasks: list):
    if not tasks:
        print("\n--- No tasks found ---")
        return

    print("\n--- Your Tasks ---")
    for task in tasks:
        status = "[✓]" if task.completed else "[ ]"
        desc = f" - {task.description}" if task.description else ""
        print(f"{status} ID: {task.id}, Title: {task.title}{desc}")
    print("------------------\n")
