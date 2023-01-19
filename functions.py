import pandas as pd
import os
import datetime
import validaciones.validacion as validacion

def obtener_datos():
    try:
        data = pd.read_csv("./recursosgenerados/csv_alta.csv")
        return data
    except FileNotFoundError:
        print("FileNotFound")

def pedir_datos ():
    data= obtener_datos()
    rango = data.at[data.index[-1],"Rank"]
    name = input("Escribe el nombre del juego: ")
    #plataforma = input("Escribe el nombre de la plataforma : ")
    plataforma = validarPlataforma(data)
    anio = validar_fecha()
    #genero = input("Escribe el genero del juego : ")
    genero = validarGenero(data)
    empresa = input("Escribe el nombre de la empresa : ")
    ventas_na = validacion.is_numero_positivo("Cantidad de ventas en Norte América : ")
    ventas_eu = validacion.is_numero_positivo("Cantidad de ventas en Europa : ")
    ventas_jp = validacion.is_numero_positivo("Cantidad de ventas en Japon : ")
    otras_ventas = validacion.is_numero_positivo("Cantida de ventas en otras localizaciones : ")
    ventas_globales = validacion.is_numero_positivo("Cantidad total de ventas contabilizadas : ")
    juego_nuevo = {"Rank":rango+1, "Name":name, "Platform":plataforma, "Year":anio, "Genre":genero, "Publisher":empresa, "NA_Sales":ventas_na, "EU_Sales":ventas_eu, "JP_Sales":ventas_jp, "Other_Sales":otras_ventas, "Global_Sales":ventas_globales}
    return juego_nuevo

def alta_juego():
    os.system('cls')
    data= obtener_datos()
    os.system('cls')
    salir="SI"
    contador=0
    while salir == "SI" or salir == "si" :
        juego_nuevo =pedir_datos()
        os.system('cls')
        respuesta=input(f"{juego_nuevo}\n ¿Datos introducidos bien? SI,NO ")
        if respuesta == "SI" or respuesta == "si":
            contador += 1
            data = data.append(juego_nuevo, ignore_index = True)
            data.to_csv("./recursosgenerados/csv_alta.csv")
            salir=input("¿Quieres introducirlo Otro? NO,SI ")
            os.system('cls')
        else:
            salir=input("¿Quieres introducirlo Otro? NO,SI ")
            os.system('cls')
    print(data.tail(contador))
    return contador

def listado_alta_juegos(datos):
    data= obtener_datos()
    if datos == "":
        print("nada")
    else:
        print(data.tail(datos))
        return data.tail(datos)

def validar_fecha():
        
        validar =  0
        while validar == 0:
            try:
                print("Introduce la fecha de lanzamiento del juego: \nTiene que ser un número comprendido entre 1952 y el año actual\n")
                fecha = int(input())
                if fecha < 1952 or fecha > datetime.datetime.today().year:
                    raise ValueError
                return fecha
            except ValueError:
                print("Numero incorrecto")
        
        # if int(fecha) > datetime.datetime.today().year:
        #     fecha = 2023
        # return fecha
            
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


def validarGenero(data):

    seguir = True
    while seguir == True:
        generos_permitidos = data.Genre.unique()
        #["Action", "Adventure", "Fighting", "Misc", "Platform", "Puzzle", "Racing", "Role-Playing", "Shooter", "Simulation", "Sports", "Strategy"]

        genero = input(f"Los generos permitidos son {generos_permitidos}\nEscribe el genero del juego: ")
        print()
        #data = obtener_datos()
        #os.system('cls')
        if genero not in generos_permitidos:
            print("Género no válido.")
        else: 
            seguir = False
            return genero

def listado_genero():
    # genero = imput
    # data= obtener_datos()
    # os.system('cls')
    # return data[(data["Genre"] == genero)]  
    data = obtener_datos()
    seguir = True
    while seguir == True:
        generos_permitidos = data.Genre.unique()
        #["Action", "Adventure", "Fighting", "Misc", "Platform", "Puzzle", "Racing", "Role-Playing", "Shooter", "Simulation", "Sports", "Strategy"]

        genero = input(f"Los generos permitidos son {generos_permitidos}\nEscribe el genero del juego: ")
        print()
        
        #os.system('cls')
        if genero not in generos_permitidos:
            print("Género no válido.")
        else: 
            seguir = False
            return data[(data["Genre"] == genero)]          
           
def validarPlataforma(data):

    seguir = True
    while seguir == True:
        plataformas_permitidas = data.Platform.unique()

        plataforma = input(f"Las plataformas permitidas son {plataformas_permitidas}\nEscribe la plataforma del juego: ")
        print()

        if plataforma not in plataformas_permitidas:
            print("Plataforma no válida.")
        else: 
            seguir = False
            return plataforma

def listado_siglo():
    data= obtener_datos()
    os.system('cls')
    siglo=validacion.is_numero_positivo("Indica los juegos del siglo que quieres ver 20 o 21: ")
    while siglo != 20 and siglo != 21:
        print("Tienes que introducir 20 o 21")
        siglo=validacion.is_numero_positivo("Indica los juegos del siglo que quieres ver 20 o 21: ")
    if siglo == 20 :
        return data[(data["Year"] > 1901) & (data["Year"] < 2000 )]
    else:
        return data[(data["Year"] > 2001) & (data["Year"] < 2100 )]
    

def esperarInput():
    print("Pulsa enter para continuar")
    input("")
    
def listar_desarrolladores():
    data = obtener_datos()
    print(data.sort_values(by="Publisher").Publisher.unique())
    
def listado_rango():
    
    data = obtener_datos()
    n1 = validacion.is_numero_positivo("Seleciona el inicio del rango desde donde quieres que se empiece a listar: ")
    n2 = validacion.is_numero_positivo("Seleciona el final del rango donde quieres que se termine el listado: ")
    print(data.iloc[n1:n2])