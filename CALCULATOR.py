import PySimpleGUI as sg
button0=sg.Button("0")#,key=0)
button1=sg.Button("1")
button2=sg.Button("2")
button3=sg.Button("3")
button4=sg.Button("4")
button5=sg.Button("5")
button6=sg.Button("6")
button7=sg.Button("7")
button8=sg.Button("8")
button9=sg.Button("9")
button10=sg.Button("10")
add_button=sg.Button("+")
sub_button=sg.Button("-")
mul_button=sg.Button("*")
div_button=sg.Button("/")

layout=[[sg.Text("Calculator app")],
        [button0,button1,button2,add_button,sub_button],
        [button3,button4,button5,mul_button,div_button]
        ,[button6,button7,button8]
        ,[button9,button10]]
windows=sg.Window("My calculator",layout,font=("Helvetica",20))
while True: 
    event,values=windows.read()
    print(event,values)
    if sg.WIN_CLOSED:
        break

# import PySimpleGUI as sg

# # Define the layout of the calculator
# layout = [
#     [sg.Input(size=(15, 1), key='input')],
#     [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('/')],
#     [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('*')],
#     [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('-')],
#     [sg.Button('0'), sg.Button('C'), sg.Button('='), sg.Button('+')],
# ]

# # Create the window
# window = sg.Window('Calculator', layout)

# # Create a variable to store the expression
# expression = ''

# # Event loop
# while True:
#     event, values = window.read()

#     # Exit if the window is closed
#     if event == sg.WIN_CLOSED:
#         break

#     # Clear input if "C" is pressed
#     if event == 'C':
#         expression = ''
#         window['input'].update(expression)

#     # Evaluate the expression if "=" is pressed
#     elif event == '=':
#         try:
#             result = str(eval(expression))
#             window['input'].update(result)
#             expression = result  # Update the expression with the result
#         except:
#             window['input'].update('Error')
#             expression = ''

#     # Otherwise, update the expression
#     else:
#         expression += event
#         window['input'].update(expression)

# # Close the window
# window.close()

