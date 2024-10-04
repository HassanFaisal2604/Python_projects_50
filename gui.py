import functions 
import PySimpleGUI as gui
label=gui.Text("Type a To-do")
input_box=gui.InputText(tooltip="Enter a todo")
add_button=gui.Button("add")
layout = [[gui.Text('My to do app')]]
window = gui.Window('My to do app', layout=[[label],[input_box,add_button]], 
                    font=('Helvetica',20))

while True:
    
    event, values=window.read()
    print(values)
    print(event)
    match event:
        case 'add':
            functions.add_task()
window.close()