from modules import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter your todo")
add_button = sg.Button("Add")

window = sg.Window("Zohaib's To-Do App.", layout=[[label], [input_box, add_button]])
window.read()
window.close()