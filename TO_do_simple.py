tasks = []

def add_task():
    user_input = input("Enter the task: ")
    tasks.append(user_input)

def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"Task {i}: {task}")

def delete_task():
    show_tasks()
    if tasks:
        try:
            task_index = int(input("Enter the task number you want to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                deleted_task = tasks.pop(task_index)
                print(f"Task '{deleted_task}' has been deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

while True:
    todo = input("Enter 'add', 'show', 'delete', or 'exit': ").lower()
    match todo:
        case 'add':
            add_task()
        case 'show':
            show_tasks()
        case 'delete':
            delete_task()
        case 'exit':
            print("The list of tasks are:", tasks)
            break
        case _:
            print("Invalid input. Please try again.")