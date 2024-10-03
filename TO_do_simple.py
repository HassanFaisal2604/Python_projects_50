import functions as fn
while True:
    todo_input = input("Enter 'add', 'show', 'delete', 'edit', or 'exit': ").lower()
    if todo_input.startswith('add'):
        task = todo_input[3:].strip()
        if task:
            fn.add_task(task)
        else:
            fn.add_task()
    elif todo_input == 'show':
        fn.show_tasks()
    elif todo_input == 'delete':
        fn.delete_task()
    elif todo_input == 'edit':
        fn.edit_task()
    elif todo_input == 'exit':
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please try again.")