def get_todos(filepath = 'files/todos.txt'):
    with open(filepath,"r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(todos_arg, filepath = "files/todos.txt"):
    with open(filepath,"w") as file:
            file.writelines(todos_arg)