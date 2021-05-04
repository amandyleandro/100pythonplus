import PySimpleGUI as sg

fondo = "#5d8aa8"
fondo_cont = "#406278"
color_b = ("#f3f4ed", "#87a96b")

def build():

    l_cont = [
        [sg.Button("CELULARES", font = ("verdana", 20), key = "-CELULARES-", border_width = 1, button_color =color_b, size = (20,2), pad = ((30,30),(35,0)))],
        
        [sg.Text("SO. a evaluar",font = ("verdana"),background_color=fondo_cont, pad = ((0,5),(0,15)))] +
        [sg.Combo(["Android", "iOS", "todos"],default_value = "todos",font = ("Verdana"), size = (7,1), pad = ((0,5),(0,15)), key = "-SO-")] +
        [sg.Spin([i for i in range(1,50)], initial_value=0, font = ("Verdana"), size = (3,1),pad = ((0,0),(0,15)), key = "-CANT1-")],
        
        [sg.Button("ZAPATILLAS \n NIKE Y ADIDAS", font = ("verdana", 20), key = "-ADIDASNIKE-", border_width = 1,button_color =color_b, size = (20,2), pad = ((30,30),(15,0)))],
        
        [sg.Text("Marca a evaluar",font = ("verdana"),background_color=fondo_cont, pad = ((0,5),(0,35)))] +
        [sg.Combo(["Adidas", "Nike", "todas"],default_value = "todas",font = ("Verdana"), size = (7,1), pad = ((0,5),(0,35)), key = "-MARCA-")] +
        [sg.Spin([i for i in range(1,50)], initial_value=0, font = ("Verdana"), size = (3,1),pad = ((0,5),(0,35)), key = "-CANT2-")],
    ]

    layout = [
        [sg.Text("DATOS PARA ANALIZAR", font=("Helvetica", 20), text_color="#f3f4ed",background_color=fondo,pad = ((0,0),(0,20)) )],
        [sg.Column(l_cont, background_color=fondo_cont, element_justification="c", pad=(0,0))],
        [sg.Button("SALIR", font = ("verdana", 20), key = "-SALIR-", border_width = 1, button_color =("#f3f4ed", fondo_cont), size = (7,1), pad = ((0,0),(15,0)))],
        
    ]

    return sg.Window("Datos para analizar", layout, background_color=fondo, element_justification="c", margins = (25,30),no_titlebar = True,)

def popup():
    sg.popup(
    "Datos Exportados",
    button_color =color_b,
    background_color=fondo,
    font = ("verdana", 15),
    button_type = None,
    no_titlebar = True,
    custom_text = "Aceptar",
    )