def add_task(task=None):
    if task is None:
        task = input("Enter the task: ").strip()
    with open('TO_do_simple.txt', 'a') as file:
        file.write(task + '\n')
        print(f"{task} has been added to the list")

def show_tasks():
    try:
        with open('TO_do_simple.txt', 'r') as file:
            tasks = file.readlines()
        if not tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"Task {i}: {task.strip()}")
    except FileNotFoundError:
        print("No tasks file found. The list is empty.")

def edit_task():
    show_tasks()
    try:
        with open('TO_do_simple.txt', 'r') as file:
            tasks = file.readlines()
        if not tasks:
            print("No tasks to edit.")
            return
        edit_index = int(input("Enter the number of the task you want to edit: ")) - 1
        if 0 <= edit_index < len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[edit_index] = new_task + '\n'
            with open('TO_do_simple.txt', 'w') as file:
                file.writelines(tasks)
            print(f"Task {edit_index + 1} has been updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    except FileNotFoundError:
        print("No tasks file found. Cannot edit tasks.")

def delete_task():
    show_tasks()
    try:
        with open('TO_do_simple.txt', 'r') as file:
            tasks = file.readlines()
        if tasks:
            try:
                task_index = int(input("Enter the task number you want to delete: ")) - 1
                if 0 <= task_index < len(tasks):
                    deleted_task = tasks.pop(task_index)
                    with open('TO_do_simple.txt', 'w') as file:
                        file.writelines(tasks)
                    print(f"Task '{deleted_task.strip()}' has been deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks to delete.")
    except FileNotFoundError:
        print("No tasks file found. Cannot delete tasks.")

while True:
    todo_input = input("Enter 'add', 'show', 'delete', 'edit', or 'exit': ").lower()
    if todo_input.startswith('add'):
        task = todo_input[3:].strip()
        if task:
            add_task(task)
        else:
            add_task()
    elif todo_input == 'show':
        show_tasks()
    elif todo_input == 'delete':
        delete_task()
    elif todo_input == 'edit':
        edit_task()
    elif todo_input == 'exit':
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please try again.")