def alta_juego(data):
    return "Alta juego"

def listado_juegos(data):
    
    #te muestra la lista de los juegos que hay en la plataforma LucaSteam
    return data[(data["Name"] == "Platform")]

def listado_nintendo(data):
    
    #Con esta funcionalidad de pandas se filtra por la columna que se escriba
    data = data[data["Publisher"] == "Nintendo"]
    #number = input("¿Cuántos registros quieres ver?")
    return data
    return #data.head()

def listado_plataforma(data):
    #data[(data["Genre"] == "Platform")]
    return data[(data["Genre"] == "Platform")]
