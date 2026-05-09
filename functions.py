import os

FILEPATH = "todos.txt"

# Create the file if it doesn't exist
if not os.path.exists(FILEPATH):
    with open(FILEPATH, "w") as file:
        pass


def get_todos(filepath=FILEPATH):
    with open(filepath,"r") as file_local:
            return file_local.readlines()


def write_todos(todo_list_arg,filepath=FILEPATH):
    with open(filepath,"w") as file:
            file.writelines(todo_list_arg)
