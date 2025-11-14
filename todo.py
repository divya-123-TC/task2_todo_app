import os

TASK_FILE = "tasks.txt"


# Load tasks from file when program starts
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        tasks = [line.strip() for line in f.readlines()]
    return tasks


# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def display_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    print("==============================")


def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        # View tasks
        if choice == "1":
            if not tasks:
                print("\nNo tasks found.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        # Add a task
        elif choice == "2":
            new_task = input("Enter a new task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print("Task added successfully.")

        # Remove a task
        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                try:
                    index = int(input("Enter task number to remove: "))
                    if 1 <= index <= len(tasks):
                        removed = tasks.pop(index - 1)
                        save_tasks(tasks)
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        # Exit
        elif choice == "4":
            print("Exiting To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1–4.")


if __name__ == "__main__":
    main()