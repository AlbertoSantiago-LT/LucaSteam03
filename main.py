import pandas as pd
import functions

def obtener_datos():
    data = pd.read_csv("vgsales.csv")
    return data

def menu():
    print("Elige una opción del menú")
    print("1. Dar de alta un juego")
    print("2. Listado general de juegoss")
    print("3. Listado de juegos de la consola Nintendo")
    print("4. Listado de juegos del género Plataforma")
    
    #HACER TRY CATCH PARA VALIDAR QUE SOLO SEA NUMEROS
    
    data = obtener_datos()
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        print(functions.alta_juego(data))
    elif opcion == "2":
        print(functions.listado_juegos(data))
    elif opcion == 3: 
        functions.listado_nintendo
    elif opcion == "4":
        print(functions.listado_plataforma(data))
        
if __name__ == "__main__": menu()