# --- Simple To-Do List ---

# empty list to store tasks
todo_list = []

# function to show all tasks
def show_tasks():
    if not todo_list:
        print("No tasks yet.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

# function to add a new task
def add_task():
    task = input("Enter task: ").strip()
    if task:
        todo_list.append(task)
        print("Task added.")
    else:
        print("Task cannot be empty.")

# function to delete a task by number
def delete_task():
    if not todo_list:
        print("No tasks to delete.")
        return
    show_tasks()
    try:
        idx = int(input("Enter task number to delete: "))
        if 1 <= idx <= len(todo_list):
            removed = todo_list.pop(idx - 1)
            print(f"Deleted: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# main menu loop
def main():
    while True:
        print("\n=== To-Do List ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

# program starts here
if __name__ == "__main__":
    main()
