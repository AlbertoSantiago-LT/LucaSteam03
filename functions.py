import pandas as pd
import os
import validaciones.validacion as validacion

def obtener_datos():
    try:
        data = pd.read_csv("./datos/vgsales.csv")
        return data
    except FileNotFoundError:
        print("FileNotFound")

def pedir_datos ():
    data= obtener_datos()
    rango = data.at[data.index[-1],"Rank"]
    name = input("Nombre Juego: ")
    plataforma = input("Nombre Plataforma: ")
    ano = validacion.is_numero_positivo("Año: ")
    genero = input("Genero del juego: ")
    empresa = input("Nombre de la empresa: ")
    ventas_na = validacion.is_numero_positivo("Ventas_NA: ")
    ventas_eu = validacion.is_numero_positivo("Ventas en EU: ")
    ventas_jp = validacion.is_numero_positivo("Ventas en JP: ")
    otras_ventas = validacion.is_numero_positivo("Otras ventas: ")
    ventas_globales = validacion.is_numero_positivo("Ventas en global: ")
    juego_nuevo = {"Rank":rango+1, "Name":name, "Platform":plataforma, "Year":ano, "Genre":genero, "Publisher":empresa, "NA_Sales":ventas_na, "EU_Sales":ventas_eu, "JP_Sales":ventas_jp, "Other_Sales":otras_ventas, "Global_Sales":ventas_globales}
    return juego_nuevo

def alta_juego():
    data= obtener_datos()
    os.system('cls')
    #obtener ultimo rango y sumar uno
    juego_nuevo =pedir_datos()
    data = data.append(juego_nuevo, ignore_index = True)
    data.to_csv("./recursosgenerados/csv_alta.csv")
    print(data.tail(4))
    return "Alta juego"

def listado_juegos():
    data= obtener_datos()
    os.system('cls')
    return data

def listado_nintendo():
    data= obtener_datos()
    os.system('cls')
    #Con esta funcionalidad de pandas se filtra por la columna que se escriba
    data = data[data["Publisher"] == "Nintendo"]
    return data

def listado_plataforma():
    data= obtener_datos()
    os.system('cls')
    return data[(data["Genre"] == "Platform")]