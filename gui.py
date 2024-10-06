import PySimpleGUI as gui
import functions

label = gui.Text('Type in a to do')
input_box = gui.InputText(tooltip='Enter task', key='todo')
add_button = gui.Button('add')

edit_button = gui.Button('edit')
Complete_button = gui.Button('Complete')
exit_button = gui.Button('exit')
display_items = gui.Listbox(values=functions.show_tasks(), enable_events=True, size=(30, 6))

layout = [
    [gui.Text('My to do app')],
    [label],
    [input_box, add_button,Complete_button],
    [display_items, edit_button,exit_button]
]
window = gui.Window('My to do app', layout, font=('Helvetica', 20))

while True:
    event, values = window.read()

    if event == 'add':
        new_todo = values['todo']  # Get the new todo from the input box
        try:
            functions.add_task(new_todo)  # Pass the new todo to the add_task function
            display_items.update(values=functions.show_tasks())  # Update the display_items with the new task
        except Exception as e:
            gui.popup(f"Error adding task: {e}", title="Error")
    
    elif event == 'edit':
        selected_items = display_items.get()  # Get the selected items from the listbox
        if selected_items:  # Check if any item is selected
            edit_val = selected_items[0]  # Get the first selected task
            new_task = gui.popup_get_text(f"Edit task '{edit_val}'", title="Edit Task")  # Prompt for new task
            if new_task:
                try:
                    functions.edit_task(edit_val, new_task)  # Call the edit_task function
                    display_items.update(values=functions.show_tasks())  # Update the display_items after editing
                except Exception as e:
                    gui.popup(f"Error editing task: {e}", title="Error")
        else:
            gui.popup("Please select a task to edit.", title="No Task Selected")
    elif event == 'Complete':
        selected_items = display_items.get()  # Get the selected items from the listbox
        if selected_items:  # Check if any item is selected
            edit_val = selected_items[0]
            delete_task=functions.delete_task(edit_val) #
            gui.popup(f" {delete_task} has been deleted")
            display_items.update(values=functions.show_tasks())
    elif event == 'exit':
        break
            
    elif event == gui.WIN_CLOSED:
        break

window.close()
