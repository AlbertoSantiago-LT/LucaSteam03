import os
import time
import functions
import validaciones.validacion as validacion

seguir = True

def menu():
    opcion = 0
    while opcion!=6:
        
        os.system("cls")
        print("\nLucaSteam03 ")
        print("**********************************************")
        print("                                             *")
        print("Elige una opción del menú                    *")
        print("1. Dar de alta un juego                      *")
        print("2. Listado general de juegos                 *")
        print("3. Listado de juegos de la consola Nintendo  *")
        print("4. Listado de juegos del género Plataforma   *")
        print("5. Mostrar juegos dados de alta              *")
        print("6. Salir                                     *")
        print("**********************************************")
       
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
        elif opcion==6:
            print("Cerrando LucaSteam03...")
        else:
            print("El numero no corresponde a ninguna accion, volviendo al menú")
            time.sleep(2.5)
        
if __name__ == "__main__": menu()
