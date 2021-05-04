import csv
import json
import os
import os.path
from collections import Counter

def evaluar_csv(arch, opc):
    dir_carp = "data"
    resultado = {}

    carpeta = os.path.join(os.getcwd(), dir_carp)
    archivo = open(os.path.join(carpeta, arch + ".csv"), "r")
    
    csv_data = csv.reader(archivo, delimiter=',')
    next(csv_data)
    datos = list(csv_data )

    if arch == "Adidas Vs Nike":
        resultado = adidasNike(datos, opc)
    else:
        resultado = celulares(datos, opc)

    guardarJson(resultado,arch)
    archivo.close()


def adidasNike(datos, opc):
    "Recive una lista de zapatillas, una o varias marcas y la cantidad de zapatillas que deseo guardar"

    zapatillas = {}
    contador = {}
    marcas, cantidad = opc

    if marcas == "todas": 
        for dat in datos:
            zapatillas[dat[1]] = { "Nombre del producto": dat[0], "Precio": dat[3], "Marca": dat[5], "Calificacion": dat[7]}
            contador[dat[1]] = dat[3]
    else:
        for dat in datos:
            if marcas in dat[5]: 
                zapatillas[dat[1]] = { "Nombre del producto": dat[0], "Precio": dat[3], "Marca": dat[5], "Calificacion": dat[7]}
                contador[dat[1]] = dat[3]

    max = dict(sorted(contador.items(), key = lambda x: float(x[1]), reverse= True)) #ordeno el diccionario por precio de mayor a menos
    
    contador = list(max)[0:int(cantidad)] #me guardo las keys de zapatillas con mayor precio

    mayores = {}
    for key in contador: #las busco y me las guardo para en la variable a retornar
        mayores[key] = zapatillas[key]

    return mayores


def celulares(datos, opc):
    "Recive una lista de celulares, uno o varios sistemas operativos y la cantidad de celulares que deseo guardar"

    celulares = {}
    contador = {}
    so, cantidad = opc

    if so == "todos": 
        for dat in datos:
            celulares[dat[2]] = { "Marca": dat[1], "os": dat[3], "Popularidad": dat[4], "Precio": dat[5],"Pantalla": dat[9], "Memoria": dat[10], "Bateria": dat[11]}
            contador[dat[2]] = dat[4]
    else:
        for dat in datos:
            if so in dat[3]: 
                celulares[dat[2]] = { "Marca": dat[1], "os": dat[3], "Popularidad": dat[4], "Precio": dat[5],"Pantalla": dat[9], "Memoria": dat[10], "Bateria": dat[11]}
                contador[dat[2]] = dat[4]

    max = dict(sorted(contador.items(), key = lambda x: float(x[1]), reverse= True)) #ordeno el diccionario por precio de mayor a menos
    
    contador = list(max)[0:int(cantidad)] #me guardo las keys de los celulares mas populares

    mayores = {}
    for key in contador:   #las busco y me las guardo para en la variable a retornar
        mayores[key] = celulares[key]

    return mayores


def guardarJson(resultado,arch):
    dir_save = "guardado"
    carpeta = os.path.join(os.getcwd(), dir_save)
    
    with open(os.path.join(carpeta, arch + ".json"), "w", encoding="utf8") as file:
        json.dump(resultado,file, indent=4, ensure_ascii=False)