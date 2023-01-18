# Importar la libreria pandas para trabajar con archivos CSV
import pandas as pd

# Funcion para listar los juegos
def listar_juegos(nombre_juego = None, plataforma = None):
    # Leer los datos del archivo CSV
    data = pd.read_csv("vgsales.csv")
    
    # Verificar si se ha especificado un nombre de juego
    if nombre_juego:
        # Filtrar los juegos por nombre
        filtered_data = data[data['Name'].str.contains(nombre_juego, case=False)]
    else:
        filtered_data = data
    # Verificar si se ha especificado una plataforma
    if plataforma:
        # Filtrar los juegos por plataforma
        filtered_data = filtered_data[filtered_data['Platform'] == plataforma]
    # Ordenar los juegos por ventas globales
    sorted_data = filtered_data.sort_values(by=['Global_Sales'], ascending=False)
    
    # Mostrar los datos
    print(sorted_data)
    
    # Verificar si hay valores nulos en los datos
    if data.isnull().values.any():
        print("Advertencia: Hay valores nulos en los datos.")

# Menu de opciones
while True:
    print("Menu de opciones")
    print("1. Juegos listados")
    print("2. Salir")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        nombre_juego = input("Ingrese el nombre del juego a listar (Dejar vacio para listar todos los juegos): ")
        plataforma = input("Ingrese la plataforma de los juegos a listar (Dejar vacio para listar todas las plataformas): ")
        listar_juegos(nombre_juego, plataforma)
    elif opcion == "2":
        break
    else:
        print("Opcion no valida.")