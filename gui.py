# Zohaib Ghumman
# 7/16/2025
# To-Do App

from modules import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter your todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("Zohaib's To-Do App.",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = values["todo"] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
window.close()