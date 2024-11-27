import FreeSimpleGUI as sg 


label1 = sg.Text("Select files to compress")
user_input1 = sg.Input()
user_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder")
user_input2 = sg.Input()
user_button2 = sg.FolderBrowse("Choose")


compress_btn = sg.Button("Compress")

window = sg.Window("File compressor", layout=[[label1,user_input1,user_button1],
                                              [label2,user_input2,user_button2],
                                              [compress_btn]])
window.read()
window.close()
