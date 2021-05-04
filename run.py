import PySimpleGUI as sg
from window import ventana
from model import utilidades as u

window = ventana.build()

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED,"Exit", "-SALIR-"):
        break

    if event in "-CELULARES-":
        u.evaluar_csv("phones_data", (values["-SO-"],values["-CANT1-"]))
        ventana.popup()
        
    if event in "-ADIDASNIKE-":
        u.evaluar_csv("Adidas Vs Nike", (values["-MARCA-"],values["-CANT2-"]))
        ventana.popup()

window.close()