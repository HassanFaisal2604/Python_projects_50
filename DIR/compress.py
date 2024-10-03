import PySimpleGUI as gui
label1=gui.Text("Select files to  Compress : ")
input1=gui.Input()
chosse_button1=gui.FileBrowse("Chosse")

label2=gui.Text("Select files to  Compress : ")
input2=gui.Input()
chosse_button2=gui.FolderBrowse("Chosse")

compress_button=gui.Button("Compress FIles")
window= gui.Window("File compressor", layout=[[label1,input1,chosse_button1],
                                              [label2,input2,chosse_button2]
                                              ,[compress_button] ])
window.read()
window.close()