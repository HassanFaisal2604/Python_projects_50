import functions 
import PySimpleGUI as gui
label=gui.Text("Type a To-do")
input_box=gui.InputText(tooltip="Enter a todo")
add_button=gui.Button("add")
layout = [[gui.Text('My to do app')], [label], [input_box, add_button]]
window = gui.Window('My to do app', layout, font=('Helvetica',20))

while True:
    event, values = window.read()
    if event == 'add':
        new_todo = values[0]  # Get the new todo from the input box
        functions.add_task(new_todo)  # Pass the new todo to the add_task function
    elif event == gui.WINDOW_CLOSED:
        break

window.close()