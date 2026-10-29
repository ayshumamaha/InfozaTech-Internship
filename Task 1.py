"""INFOZATECH Task 1: To-Do List Application
Run with: python task1_todo_list.py
Tasks are saved in tasks.json in the same directory.
"""
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read saved tasks. Starting with an empty list.")
        return []


def save_tasks(tasks):
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
    except OSError as error:
        print(f"Could not save tasks: {error}")


def show_tasks(tasks):
    if not tasks:
        print("\nYour task list is empty.")
        return
    print("\n--- TO-DO LIST ---")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f'{index}. [{status}] {task["title"]}')


def choose_task(tasks, prompt):
    if not tasks:
        print("There are no tasks to select.")
        return None
    show_tasks(tasks)
    try:
        number = int(input(prompt).strip())
        if 1 <= number <= len(tasks):
            return number - 1
    except ValueError:
        pass
    print("Please enter a valid task number.")
    return None


def main():
    tasks = load_tasks()
    while True:
        print("\n===== TO-DO LIST APPLICATION =====")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            title = input("Enter task description: ").strip()
            if not title:
                print("Task description cannot be empty.")
                continue
            tasks.append({"title": title, "completed": False})
            save_tasks(tasks)
            print("Task added successfully.")
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            index = choose_task(tasks, "Enter task number to complete: ")
            if index is not None:
                tasks[index]["completed"] = True
                save_tasks(tasks)
                print("Task marked as completed.")
        elif choice == "4":
            index = choose_task(tasks, "Enter task number to delete: ")
            if index is not None:
                removed = tasks.pop(index)
                save_tasks(tasks)
                print(f'Task "{removed["title"]}" deleted.')
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option. Choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
