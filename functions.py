def alta_juego(data):
    return "Alta juego"

def listado_juegos(data):
    return "Listado juegos"

def listado_nintendo(data):
    return "Nintendo"

def listado_plataforma(data):
    #data[(data["Genre"] == "Platform")]
    return data[(data["Genre"] == "Platform")]
