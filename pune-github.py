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
def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")


 if choice == "1":
            if not tasks:
                print("No tasks found.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    status = "✅" if task.endswith("[Done]") else "⏳"
                    print(f"{i}. {task.replace(' [Done]', '')} [{status}]")

 elif choice == "2":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!")

