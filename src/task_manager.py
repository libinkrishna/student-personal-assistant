import json
from pathlib import Path

DATA_FILE = Path("data/tasks.json")

def load_tasks():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def manage_tasks():
    while True:
        print("\nTask Manager:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            tasks = load_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
        elif choice == "2":
            task = input("Enter the task: ")
            tasks = load_tasks()
            tasks.append(task)
            save_tasks(tasks)
            print("Task added successfully.")
        elif choice == "3":
            tasks = load_tasks()
            if not tasks:
                print("No tasks to delete.")
            else:
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
                to_delete = int(input("Enter the task number to delete: "))
                if 1 <= to_delete <= len(tasks):
                    removed = tasks.pop(to_delete - 1)
                    save_tasks(tasks)
                    print(f"Task '{removed}' deleted.")
                else:
                    print("Invalid task number.")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
