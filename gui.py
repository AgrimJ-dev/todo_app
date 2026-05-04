import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter task", key="todo")
add_button = sg.Button("Add")
label2 = sg.Text("Remaining Tasks:")
list_box = sg.Listbox(values=functions.get_todos(), key="tasks",
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

layout = [[label], 
          [input_box, add_button],
          [label2],
          [list_box, edit_button]
          ]

window = sg.Window("todo app",
                   layout=layout,
                   font=('Helvetica',18))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['tasks'].update(values=todos)

        case "Edit":
           todo_to_edit = values['tasks'][0]
           new_todo = values['todo'] + "\n"

           todos = functions.get_todos()
           index = todos.index(todo_to_edit)
           todos[index] = new_todo
           functions.write_todos(todos)

           window['tasks'].update(values=todos)

        case "tasks":
            window['todo'].update(value=values['tasks'][0])

        case sg.WIN_CLOSED:
            break

window.close()
