import func 

while True:
    todo_input = input("Enter 'add', 'show', 'delete', 'edit', or 'exit': ").lower()
    if todo_input.startswith('add'):
        task = todo_input[3:].strip()
        if task:
            func.add_task(task)
        else:
            func.add_task()
    elif todo_input == 'show':
        func.show_tasks()
    elif todo_input == 'delete':
        func.delete_task()
    elif todo_input == 'edit':
        func.edit_task()
    elif todo_input == 'exit':
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please try again.")