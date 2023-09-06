# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

from cod_generator import generar

def generar_codigo():
    codigo_generado = generar()
    return codigo_generado

def nuevo_libro(autor, titulo, cant_ej_adquiridos):
    codigo = generar_codigo()  # Genera un código para el nuevo libro
    libro_nuevo = {
        'cod': codigo,
        'autor': autor,
        'titulo': titulo,
        'cant_ej_ad': cant_ej_adquiridos,
        'cant_ej_pr': 0
        }  # Inicialmente, no hay ejemplares prestados

        
        
    print("Libro registrado con éxito:")
    print(f"Código: {codigo}")
    print(f"Autor: {autor}")
    print(f"Título: {titulo}")
    print(f"Cantidad de ejemplares adquiridos: {cant_ej_adquiridos}")

    return libro_nuevo






