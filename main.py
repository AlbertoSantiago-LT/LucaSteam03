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
        print(Fore.YELLOW + "2. Listado general de juegos                 *")
        print(Fore.YELLOW + "3. Listado de juegos de la consola Nintendo  *")
        print(Fore.YELLOW + "4. Listado de juegos del género Plataforma   *")
        print(Fore.YELLOW + "5. Mostrar juegos dados de alta              *")
        print(Fore.YELLOW + "6. Salir                                     *")
        print(Fore.RESET + "**********************************************")
       
        opcion = validacion.is_numero_positivo("Seleccione una opcion: ")
        if opcion == 1:
            functions.alta_juego()
            functions.esperarInput()
        elif opcion == 2:
            print(functions.listado_juegos())
            functions.esperarInput()
        elif opcion == 3: 
            print(functions.listado_nintendo())
            functions.esperarInput()
        elif opcion == 4:
            print(functions.listado_plataforma())
            functions.esperarInput()
        elif opcion==0:
            print("Cerrando LucaSteam03...")
        else:
            print("El numero no corresponde a ninguna accion, volviendo al menú")
            time.sleep(2.5)
        
if __name__ == "__main__": menu()
