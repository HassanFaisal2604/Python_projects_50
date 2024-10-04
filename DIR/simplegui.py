import PySimpleGUI as sg

# Create the window layout
label1 = sg.Text("Enter feet : ")
feet_input = sg.Input()
convert_button = sg.Button('Convert')
layout = [[label1, feet_input], [convert_button]]

# Create the window
window = sg.Window('Feet to Inches Converter', layout)

# Event loop
event, values = window.read()
window.close()

# Handle the button event
if event == 'Convert':
    try:
        # Get the input value from 'values' dictionary and convert to float
        feet_value = float(values[0])  # Extracts the input from the first input field
        total_inches = feet_value * 12
        sg.popup(f'Total Inches: {total_inches}')
    except ValueError:
        sg.popup('Please enter a valid number.')
