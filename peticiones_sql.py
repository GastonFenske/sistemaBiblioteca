import funciones_sql

def consultar_todos_los_libros_disponibles():
    print('Los libros disponibles a continuacion:\n')
    for libro in funciones_sql.mostrar_libros_disponibles():
        print('Nombre: {}, autor: {}, año: {}, paginas: {}'.format(libro[1], libro[2], libro[3], libro[4]))


def consultar_libros_de_un_cliente():

    for cliente in funciones_sql.mostrar_clientes():
        print('Cliente con ID: [{}]      llamado: {} {}'.format(cliente[0], cliente[1], cliente[2]))

    idcliente = int(input('Ingrese el ID del cliente: '))

    print('El libro {}, lo tiene el cliente llamado {}'.format(funciones_sql.mostrar_libros_de_un_cliente(idcliente)[0][0], funciones_sql.mostrar_libros_de_un_cliente(idcliente)[0][1]))

def consultar_un_determinado_libro():

    for libro in funciones_sql.mostrar_libros():
        print('Libro con ID: [{}]       llamado: {}'.format(libro[0], libro[1]))

    idlibro = int(input('Ingrese el ID del libro: '))

    print('Ese libro lo tiene el cliente llamado {}'.format(funciones_sql.mostrar_quien_tiene_un_libro(idlibro)))


def eliminar_las_asginaciones():
    funciones_sql.eliminar_asignaciones()
    print('Asignaciones eliminadas')

def eliminar_todos_los_libros():
    funciones_sql.eliminar_libros()
    print('Libros eliminados')

def eliminar_todos_los_clientes():
    funciones_sql.eliminar_clientes()
    print('Clientes eliminados')