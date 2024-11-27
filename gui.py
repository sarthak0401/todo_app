import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in the todo")
input_box  = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")

window = sg.Window("My todo-app", layout=[[label],[input_box,add_button]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == "Add":
        todos = functions.get_todos()
        todos.append(values['todo'] + '\n')
        functions.write_todo(todos)
    
    elif event == sg.WIN_CLOSED:
        break

window.close()