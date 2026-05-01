import functions
import FreeSimpleGUI as sg

sg.theme("DarkBlack") 

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter task", key="todo")
add_button = sg.Button("Add")

layout = [[label], [input_box, add_button]]

window = sg.Window("todo app",
                   layout,
                   font=('Helvetica',20))
event, values = window.read()
print(event)
print(values)
window.close()
