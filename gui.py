import functions 
import PySimpleGUI as gui

label = gui.Text("Type a To-do")
input_box = gui.InputText(tooltip="Enter a todo")
add_button = gui.Button("add")
show_button = gui.Button("show")
edit_button = gui.Button("edit")
display_items = gui.Listbox(values=functions.show_tasks(),
                            enable_events=True, size=(45,10))

layout = [[gui.Text('My to do app')], [label], [input_box, add_button, show_button], [display_items, edit_button]]
window = gui.Window('My to do app', layout, font=('Helvetica', 20))

while True:
    event, values = window.read()
    if event == 'add':
        new_todo = values[0]  # Get the new todo from the input box
        functions.add_task(new_todo)  # Pass the new todo to the add_task function
        display_items.update(values=functions.show_tasks())  # Update the display_items with the new task
    elif event == 'edit':
        selected_items = display_items.get()  # Get the selected items from the listbox
        if selected_items:  # Check if any item is selected
            edit_val = selected_items[0]  # Get the first selected task
            functions.edit_task(edit_val)  # Call the edit_task function with the selected task
            display_items.update(values=functions.show_tasks())  # Update the display_items after editing
        else:
            gui.popup("Please select a task to edit.", title="No Task Selected")  # Notify user to select a task
    elif event == 'show':
        todos = functions.show_tasks()
        if todos:  # Check if todos is not empty before creating a popup
            gui.popup('Tasks are shown', title='Your tasks', content=todos)
        else:
            gui.popup('No tasks to show', title='Your tasks')
    elif event == gui.WIN_CLOSED:
        break

window.close()