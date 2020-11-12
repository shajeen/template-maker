import PySimpleGUI as gui
import shutil
import json
import os

gui.theme('DarkAmber')

layout = [[gui.Text('Project name:'), gui.InputText()],
          [gui.Text("Choose a folder: "), gui.Input(key="-IN1-" ,change_submits=True), gui.FolderBrowse(key="-IN-")],
          [gui.Button('Create'), gui.Button('Abort')]]

window = gui.Window('conan application project structure creator', layout)

def write_file(write_file, values):
    with open(write_file) as f:
        newText = f.read().replace('example', values)        
    with open(write_file, "w") as f:
        f.write(newText)

def create_structure(values):
    with open('configuration/conan_application.json') as file:
        data = json.load(file)
    for d in data['file']:
        dest = values['-IN1-']+'/'
        if dest == '/':
            if not os.path.isdir('out'):
                 os.mkdir('out')
            dest = os.path.dirname(os.path.realpath(__file__))+'/out/'
        shutil.copy2(d["path"], dest)
        if d["name"] == "CMakeLists.txt" or d["name"] == "README.md":
            write_file(dest+d["name"], values[0])


while True:
    events, values = window.read()
    if events == gui.WIN_CLOSED or events == 'Abort':
        break
    elif events == 'Create':
        create_structure(values)
        break

window.close()
