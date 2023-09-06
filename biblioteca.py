import libro as l

# Crear una lista vacía para almacenar los libros
libros = [l.libro1,l.libro2,l.libro3]

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

#Funcion que verifica si quedan ejemplares o no.

def ejemplares_prestados(libro_actual):
    if libro_actual['cant_ej_ad'] <= 0:
        print("NO QUEDAN EJEMPLARES PARA PRESTAR")

    elif libro_actual['cant_ej_ad'] > 0:
        print("QUEDAN EJEMPLARES")

def registrar_nuevo_libro(autor, titulo, cant_ej_adquiridos):
    nuevo_libro = l.nuevo_libro(autor, titulo, cant_ej_adquiridos)
    libros.append(nuevo_libro)
    print(libros)

#Funcion para eliminar ejemplares. 

def eliminar_ejemplar_libro(codigo):
    for libro_actual in libros:
        if codigo == libro_actual['cod']:
            book = libro_actual['cant_ej_ad']
            if book > 0:
                libro_actual['cant_ej_ad'] -= 1
                print(f"Se ha eliminado correctamente el libro {libro_actual['titulo']}")
                break

            else:
                print("No hay libros para eliminar ")
                break    
    

def prestar_ejemplar_libro(codigo, lista_libros):
    
    for libro_actual in libros:
        
        if codigo == libro_actual['cod']:
           
            if libro_actual['cant_ej_ad'] >= libro_actual['cant_ej_pr']:
                libro_actual['cant_ej_pr'] += 1
                libro_actual['cant_ej_ad'] -= 1
                print("Ha realizado la adquisicion del libro correctamente")
                break

            else:
                print("No hay libros disponibles")
                break    

                    
def devolver_ejemplar_libro(codigo):
    for libro_actual in libros:
        if codigo == libro_actual['cod']:
            if libro_actual['cant_ej_pr'] > 0:
                print("Se ha realizado la devolucion")
                libro_actual['cant_ej_pr'] -= 1
                libro_actual['cant_ej_ad'] += 1
                break    

            else:
                print("No hay ejemplares prestados para devolver")
                break


def mostrar_ejemplares_prestados():
    hay_ejemplares_prestados = False  
    
    for libro_actual in libros:
        if libro_actual['cant_ej_pr'] > 0:
            print(f"Libro: {libro_actual['titulo']}, Cantidad de ejemplares prestados: {libro_actual['cant_ej_pr']}")
            hay_ejemplares_prestados = True  
    
    if not hay_ejemplares_prestados:
        print("No hay ejemplares prestados de ningún libro.")

 
""" 
def nuevo_libro():
    Esta funcion no la utilizamos ya que usamos la misma funcion nuevo_libro en el modulo de "Libro.py"...
    La funcion biblioteca.registrar_nuevo_libro(autor, titulo, cant_ej_adquiridos) recibe los 3 parametros y estos mismos parametros los utilizamos para asignar
    autor, titulo y cantidad de ejemplares adquiridos
    return None
"""  







