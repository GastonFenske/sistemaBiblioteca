from asignaciones import Asginacion
import funciones_sql

def agregar_asignacion_a_la_base(id_cliente, id_libro, fecha):
    asignacion = Asginacion(id_cliente, id_libro, fecha)
    funciones_sql.insertar_asginacion_en_la_base(asignacion)

def datos_para_agregar_asignacion():
    for cliente in funciones_sql.mostrar_clientes():
        print('Cliente con ID: [{}]      llamado: {} {}'.format(cliente[0], cliente[1], cliente[2]))

    id_cliente = int(input('Ingrese el ID del cliente: '))
    
    for libro in funciones_sql.mostrar_libros():
        print('Libro con ID: [{}]       de nombre: {}'.format(libro[0], libro[1]))

    id_libro = int(input('Ingrese el ID del libro: '))

    fecha = str(input('Ingrese la fecha de la asignacion: '))

    agregar_asignacion_a_la_base(id_cliente, id_libro, fecha)