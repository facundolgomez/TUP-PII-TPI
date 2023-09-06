# Trabajo Práctico I - Programación II


import os
import libro
import biblioteca


       
    



def encontrar_libro(codigo):
    # Accede a los diccionarios de libros desde el módulo "libro"
    libros = [libro.libro1, libro.libro2, libro.libro3]
    
    for libro_actual in libros:
        if codigo == libro_actual['cod']:
            print(f"Autor: {libro_actual['autor']}")
            print(f"Título: {libro_actual['titulo']}")
            print(f"Cantidad de ejemplares disponibles: {libro_actual['cant_ej_ad']}")

            biblioteca.ejemplares_prestados(libro_actual)

            confirmacion = int(input(f"Desea confirmar la adquisicion del libro {libro_actual['titulo']}, 1 para confirmar el prestamo, 0 para salir "))
            while confirmacion != 1 and confirmacion != 0:
                print("Ingrese 1 o 0")
                confirmacion = int(input())

            if confirmacion == 1:
                biblioteca.prestar_ejemplar_libro(codigo,libro_actual)
                
                
            else:
                print("Operacion cancelada")       
            
            break

        else:
            print("No existe el codigo de ese libro")
            break     







        



   
        


print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Elimiar ejemplar")
    print("5 - Mostrar ejemplares prestados")
    print("6 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            #completar
            codigo = input("Ingrese el codigo del libro ")
            encontrar_libro(codigo)
        elif int(opt) == 2:
            #completar
            codigo = input("Ingrese el codigo del libro que quiere devolver ")
            biblioteca.devolver_ejemplar_libro(codigo)

        elif int(opt) == 3:
            autor = input("Ingrese el autor del libro: ")
            while autor == "":
                print("No puede dejar este campo vacío. Por favor, ingrese un valor.")
                autor = input("Autor:")
            titulo = input("Ingrese el título del libro: ")
            while titulo == "":
                print("No puede dejar este campo vacío. Por favor, ingrese un valor.")
                titulo = input("titulo:")
            cant_ej_adquiridos = int(input("Ingrese la cantidad de ejemplares adquiridos "))
            while cant_ej_adquiridos <= 0:
                cant_ej_adquiridos = int(input("Ingrese una cantidad valida "))
            biblioteca.registrar_nuevo_libro(autor, titulo, cant_ej_adquiridos)
            
        elif int(opt) == 4:
            codigo = input("Ingrese el codigo del libro ")
            biblioteca.eliminar_ejemplar_libro(codigo)
        elif int(opt) == 5:
            biblioteca.mostrar_ejemplares_prestados()
        elif int(opt) == 6:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")













           


