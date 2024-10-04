import time

print(f"Today's date is {time.strftime('%b/%m/%y')}")

def read_file(filepath='TO_do_simple.txt'):
    try:
        with open(filepath, 'r') as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]  # Return stripped tasks
    except FileNotFoundError:
        return []

def add_task(task):
    task = task.strip()  # Ensure no leading/trailing whitespace
    with open('TO_do_simple.txt', 'a') as file:
        file.write(task + '\n')
        print(f"{task} has been added to the list")

def show_tasks():
    tasks = read_file()
    return tasks  # Return list of tasks to be displayed

def edit_task(old_task, new_task):
    tasks = read_file()
    try:
        task_index = tasks.index(old_task.strip())  # Find the old task
        tasks[task_index] = new_task.strip()  # Replace with the new task
        with open('TO_do_simple.txt', 'w') as file:
            file.writelines([task + '\n' for task in tasks])  # Write back tasks
        print(f"Task '{old_task}' has been updated to '{new_task}'")
    except ValueError:
        print("Task not found.")

def delete_task():
    tasks = read_file()
    if tasks:
        try:
            task_index = int(input("Enter the task number you want to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                deleted_task = tasks.pop(task_index)
                with open('TO_do_simple.txt', 'w') as file:
                    file.writelines([task + '\n' for task in tasks])
                print(f"Deleted task: {deleted_task.strip()}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks to delete.")
