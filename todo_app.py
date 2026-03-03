import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.\n")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    tasks = load_tasks()

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()
