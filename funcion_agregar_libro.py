from libros import Libro
import funciones_sql


def agregar_libro_al_catalogo(nombre, autor, año, cantidad_de_paginas):
    libro = Libro(nombre, autor, año, cantidad_de_paginas)
    funciones_sql.ingresar_libro_en_la_base(libro)

def datos_para_agregar_libro():
    nombre = str(input('Ingrese el nombre del libro: '))
    autor = str(input('Ingrese el autor del libro: '))
    año = int(input('Ingrese el año del libro: '))
    cantidad_paginas = int(input('Ingrese cantidad de paginas del libro: '))

    agregar_libro_al_catalogo(nombre, autor, año, cantidad_paginas)
