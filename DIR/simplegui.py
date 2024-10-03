import PySimpleGUI as sg

label1=sg.Text("Enter feet : ")
feet_input=sg.Input()

label2=sg.Text("Enter Inches :")
Inches_input=sg.Input()
convert_button = sg.Button('Convert')
output=sg.Window('feet to inches converter',layout=[[label1,feet_input],[label2,Inches_input],[convert_button]])

event, values = output.read()
output.close()

if event == 'Convert':
    feet = float(feet_input.get())
    inches = float(Inches_input.get())
    total_inches = (feet * 12) + inches
    sg.popup(f'Total Inches: {total_inches}')
