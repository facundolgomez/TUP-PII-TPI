import libro as l


# Crear una lista vacía para almacenar los libros
libros = [l.libro1,l.libro2,l.libro3]

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)








def ejemplares_prestados(libro_actual):
    if libro_actual['cant_ej_ad'] <= 0:
        print("NO QUEDAN EJEMPLARES PARA PRESTAR")

    elif libro_actual['cant_ej_ad'] > 0:
        print("QUEDAN EJEMPLARES")

        

    


def registrar_nuevo_libro(autor, titulo, cant_ej_adquiridos):
    nuevo_libro = l.nuevo_libro(autor, titulo, cant_ej_adquiridos)
    libros.append(nuevo_libro)
    print(libros)
    
        


def eliminar_ejemplar_libro():
    #completar
    return None




def prestar_ejemplar_libro(codigo, lista_libros):
    #completar
    
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







def nuevo_libro():
    
    return None







