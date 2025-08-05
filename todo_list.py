todo_list = []
def show_menu():
    print("Todo List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task ")
    print("4. Remove a task")
    print("5. Exit")

    def add_task():
        task = input("Enter the task to add: ")
        todo_list.append({"task": task, "done": False})
        print("Task Succefully Added")

    def view_tasks():
        if not todo_list:
            print("No tasks available.")
        else:
            print("\n Your tasks:")
            for index, task in enumerate(todo_list, start=1):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index}. {task['task']} - [{status}]")
    def mark_done():
        view_tasks()
        try:
            task_no = int(input("Enter the task number to mark as done: ")) 
            todo_list[task_no - 1]["done"] = True
            print("Task marked as done.")   
        except:
                print("invalid input.")
    def delete_task():
        view_tasks()
        try:
            task_no = int(input("Enter the task number to remove: "))
            del todo_list[task_no - 1]
            print("Task deleted.")
        except:
            print("Invalid input.")

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
            print("Bye")
            break
        else:
            print("Invalid choice. Please try again.")
           