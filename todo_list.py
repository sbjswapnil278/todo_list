todo_list = []

def show_menu():
    print("\nTodo List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as done")
    print("4. Remove a task")
    print("5. Exit")

def add_task():
    task = input("Enter the task to add: ")
    todo_list.append({"task": task, "done": False})
    print("Task successfully added.")

def view_tasks():
    if not todo_list:
        print("No tasks available.")
    else:
        print("\nYour tasks:")
        for index, task in enumerate(todo_list, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{index}. {task['task']} - [{status}]")

def mark_done():
    view_tasks()
    try:
        task_no = int(input("Enter the task number to mark as done: ")) 
        if 1 <= task_no <= len(todo_list):
            todo_list[task_no - 1]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter the task number to remove: "))
        if 1 <= task_no <= len(todo_list):
            del todo_list[task_no - 1]
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
