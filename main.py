import os
import time
import functions
import validaciones.validacion as validacion
from colorama import Fore, Style
from pyfiglet import Figlet

seguir = True

def menu():
    opcion = -1
    while opcion!=0:
        
        os.system("cls")
        f = Figlet(font='slant')
        print(Fore.GREEN + f.renderText("LucaSteam03"))
        print("**********************************************")
        print("                                             *")
        print(Fore.BLUE + "Elige una opción del menú                    *")
        print(Fore.YELLOW + "1. Dar de alta un juego                      *")
        print(Fore.YELLOW + "2. Elegir tipo de informe                    *")
        print(Fore.YELLOW + "0. Salir                                     *")
        print(Fore.RESET + "**********************************************")
       
        opcion = validacion.is_numero_positivo("Seleccione una opcion: ")
        if opcion == 1:
            functions.alta_juego()
            functions.esperarInput()
        elif opcion == 2:
            menu_listados()
        elif opcion==0:
            print("Cerrando LucaSteam03...")
        else:
            print("El numero no corresponde a ninguna accion, volviendo al menú")
            time.sleep(1.5)
        
        
        
def menu_listados():
    opcion = -1
    while opcion!=0:
        os.system("cls")
        f = Figlet(font='slant')
        print(Fore.GREEN + f.renderText("Informes de LucaSteam03"))
        print("**********************************************")
        print("                                             *")
        print(Fore.YELLOW + "1. Listado general de juegos                 *")
        print(Fore.YELLOW + "2. Listado de juegos de la consola Nintendo  *")
        print(Fore.YELLOW + "3. Listado de juegos del género Plataforma   *")
        print(Fore.YELLOW + "4. Listado de juegos dados de alta           *")
        print(Fore.YELLOW + "4. Listado de juegos dado un rango a elegir  *")
        print(Fore.YELLOW + "5. Listado de desarrolladores de los juegos  *")
        print(Fore.YELLOW + "6. Listado filtrado por siglo                *")
        print(Fore.YELLOW + "7. Listado filtrado por género               *")
        print(Fore.YELLOW + "0. Salir                                     *")

        opcion = validacion.is_numero_positivo("Seleccione una opcion: ")
        if opcion == 1: 
            print(functions.listado_juegos())
            functions.esperarInput()
        elif opcion == 2:
            print(functions.listado_nintendo())
            functions.esperarInput()       
        elif opcion == 3:
            print(functions.listado_plataforma())
            functions.esperarInput() 
        elif opcion == 4:
            print(functions.listado_alta_juegos())
            functions.esperarInput() 
        elif opcion == 5:
            print(functions.listar_desarrolladores())
            functions.esperarInput()  
        elif opcion == 6:
            print(functions.listado_siglo())
            functions.esperarInput() 
        elif opcion == 7:
            print(functions.listado_genero())
            functions.esperarInput() 
        elif opcion == 0:
            print("Volviendo al menú principal de LucaSteam03...")
            time.sleep(1.5)
        else:
            print("El numero no corresponde a ninguna accion, volviendo al menú")
            time.sleep(1.5)

if __name__ == "__main__": menu()