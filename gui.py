import functions
import FreeSimpleGUI as sg
import time


sg.theme("Black")

clock = sg.Text("", key="clock")

label = sg.Text("Type in the todo")

input_box = sg.InputText(tooltip="Enter todo", key='todo')

add_button = sg.Button("Add")

# Strip '\n' for display in the list_box
list_box = sg.Listbox(
    values=list(map(lambda x: x.strip("\n"), functions.get_todos())), 
    key='todox', 
    enable_events=True, 
    size=[45, 10]
)

edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

window = sg.Window(
    "My todo-app", 
    layout=[[clock],[label], 
            [input_box, add_button], 
            [list_box, edit_button, complete_button],
            [exit_button]],
    font=("Helvetica", 13)
)

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d,%Y - %H:%M:%S"))
    if event == sg.WIN_CLOSED:
        break

    if event == "Add":
        # Add new todo
        new_todo = values['todo']
        if new_todo.strip():  # Ensure input is not empty
            todos = functions.get_todos()
            todos.append(new_todo + '\n')  # Add with '\n' for file storage
            functions.write_todo(todos)

            # Update Listbox without '\n'
            window['todox'].update(values=list(map(lambda x: x.strip("\n"), todos)))

    elif event == "Edit":
        # Edit selected todo
        try:
            todo_to_edit = values['todox'][0]  # Get selected todo
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit + '\n')  # Find the original item with '\n'
            todos[index] = new_todo + '\n'  # Update with new value
            functions.write_todo(todos)

            # Update Listbox without '\n'
            window['todox'].update(values=list(map(lambda x: x.strip("\n"), todos)))
        except IndexError:
            sg.popup("Please select an item to edit.")

    elif event == "Complete":
        try:
            todo_to_complete = values['todox'][0]  # Get selected todo
            todos = functions.get_todos()
            todos.remove(todo_to_complete + '\n')
            functions.write_todo(todos)
            window['todox'].update(values=list(map(lambda x: x.strip("\n"), todos)))
            window['todo'].update(value="")
        except IndexError:
            sg.popup("Please select a todo to complete")


    elif event == "Exit":
        break

    elif event == 'todox':
        # Update input box with selected todo
        try:
            window['todo'].update(value=values['todox'][0])
        except IndexError:
            pass

window.close()
