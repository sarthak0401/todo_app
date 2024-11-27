# from functions import get_todos, write_todo
# we can call this approach if there are very less functions

from modules import functions
import time 

print(f"Today is : {time.strftime("%b %d,%Y - %H:%M:%S")}")

while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.strip()     
    # OR we can simply use the below command   -> these will remove the trailing and the starting spaces from the input, with this we can give input as '       add          ' as well
    # user_action = input("Enter add, show or exit: ").strip()
    
    if user_action.startswith("add"):
        # todo = input("Enter the todo: ") + "\n"
        
        # file  = open('files/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        # We dont need to close the file with "with" keyword
        todos = functions.get_todos()

        todos.append(user_action[4:]+'\n')

        functions.write_todo(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        # new_todos = [item.strip("\n") for item in todos]
        # for index, item in enumerate(new_todos):
        #     print(f"{index+1}. {item}")
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index+1}-{item}")
    
    # elif 'edit' in user_action:    this gives error when user enters edit add a list   -> this will add it instead, not edit
    elif user_action.startswith("edit"):
        try:
            # Learnt to do the type conversion, as input function in python is by default a "STRING"
            # number = int(input("Enter the number of the todo to edit: "))
            number = int(user_action[5:])
            
            todos = functions.get_todos()

            print(f"The current todo is {todos[number-1].strip("\n")}")
            # Learnt also to access the list element and modify it

            todos[number-1] = input("Enter the new edited todo: ") + '\n'

            functions.write_todo(todos)

        except ValueError:
            print("Enter the command again")
            continue


    elif user_action.startswith("complete"):
        try:
            # number = int(input("Enter the number of the todo to be marked completed: "))
            number = int(user_action[9:])

            todos = functions.get_todos()
            
            todo_to_be_removed = todos[number-1]
            todos.pop(number-1)

            functions.write_todo(todos)
            print(f"Todo '{todo_to_be_removed.strip("\n")}' was removed from the list")
        except IndexError:
            print("Enter the correct index")
        

    elif 'exit' in user_action:
        break
    
    else:
        print("Enter a valid command!")

print("bye!")
