import os
def alta_juego(data):
    os.system('cls')
    return "Alta juego"

def listado_juegos(data):
    os.system('cls')
    return data

def listado_nintendo(data):
    os.system('cls')
    
    #Con esta funcionalidad de pandas se filtra por la columna que se escriba
    data = data[data["Publisher"] == "Nintendo"]
    #number = input("¿Cuántos registros quieres ver?")
    return data
    return #data.head()

def listado_plataforma(data):
    os.system('cls')
    #data[(data["Genre"] == "Platform")]
    return data[(data["Genre"] == "Platform")]