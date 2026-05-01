FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath,"r") as file_local:
            return file_local.readlines()


def write_todos(todo_list_arg,filepath=FILEPATH):
    with open(filepath,"w") as file:
            file.writelines(todo_list_arg)
