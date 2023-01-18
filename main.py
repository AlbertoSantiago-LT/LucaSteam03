import os
import functions
import validaciones.validacion as validacion
from termcolor import colored

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored("*********************************************", "green"))
    print(colored("***Elige una opción del menú***", "green", attrs=["bold"]))
    print(colored("*********************************************", "green"))
    print(colored("1. Dar de alta un juego", "blue", attrs=["bold"]))
    print(colored("2. Listado general de juegos", "blue", attrs=["bold"]))
    print(colored("3. Listado de juegos de la consola Nintendo", "blue", attrs=["bold"]))
    print(colored("4. Listado de juegos del género Plataforma", "blue", attrs=["bold"]))

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
