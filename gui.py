import functions
import FreeSimpleGUI as sg
import time

sg.theme("Black")


clock = sg.Text("",key = "clock")
label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter task", key="todo")
add_button = sg.Button("Add")
label2 = sg.Text("Remaining Tasks:")
list_box = sg.Listbox(values=functions.get_todos(), key="tasks",
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[clock],
          [label], 
          [input_box, add_button],
          [label2],
          [list_box, edit_button, complete_button],
          [exit_button]
          ]

window = sg.Window("todo app",
                   layout=layout,
                   font=('Helvetica',18))
while True:
    event, values = window.read(timeout=400)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()   
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['tasks'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['tasks'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)

                window['tasks'].update(values=todos)

            except IndexError:
                sg.popup("Please select an item to edit first",font=("Helvetica",20))

        case "Complete":
            try:
                todo_to_complete = values['tasks'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)

                window['tasks'].update(values=todos)
                window['todo'].update(value='')

            except IndexError:
                sg.popup("Please select an item to edit first",font=("Helvetica",20))

        case "Exit":
            break

        case "tasks":
            window['todo'].update(value=values['tasks'][0])

        case sg.WIN_CLOSED:
            break

window.close()
