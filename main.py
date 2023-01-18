import os
import functions
import validaciones.validacion as validacion

def menu():
    print("Elige una opción del menú")
    print("1. Dar de alta un juego")
    print("2. Listado general de juegos")
    print("3. Listado de juegos de la consola Nintendo")
    print("4. Listado de juegos del género Plataforma")
    
    #HACER TRY CATCH PARA VALIDAR QUE SOLO SEA NUMEROS

    #data = obtener_datos()
    #opcion = input("Seleccione una opcion: ")
    opcion = validacion.is_numero_positivo("Seleccione una opcion: ")
    if opcion == 1:
        functions.alta_juego()
    elif opcion == 2:
        print(functions.listado_juegos())
    elif opcion == 3: 
        print(functions.listado_nintendo())
    elif opcion == 4:
        print(functions.listado_plataforma())
    else:
        print("El numero no corresponde a ninguna accion")
        
if __name__ == "__main__": menu()
