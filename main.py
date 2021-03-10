import PySimpleGUIQt as sg
import subprocess, sys
import os

layout = [
    [sg.Text("Choose what you would like to install")],
    [sg.Button("Install Fabric")],
    [sg.Button("Install Mods Only")],
    [sg.Button("Install Everything")],
]

layout2 = [
    [sg.Text("Do you want to delete all your existing mods in ~/AppData/Roaming/.minecraft and install the Beginnings SMP Mods?")],
    [sg.Yes(), sg.No()],
]

window = sg.Window("Beginnings SMP", layout)
window2 = sg.Window("Are you sure?", layout2)

while True:
    window2 = event, values = window2.read()
    if event in "No":
        break

    window = event, values = window.read()

    if event in "Install Fabric":
        os.system('"./fabric-installer-0.7.2.exe"')
        print(os.environ['USERNAME'])
    if event in "Install Mods Only":
        break
    if event in "Install Everything":
        break

exit()
