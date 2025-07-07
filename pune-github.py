import os

TODO_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]



# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display menu
def show_menu():
    print("\n===== To-Do List App =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark task as completed")
    print("5. Search task")
    print("6. Exit")
