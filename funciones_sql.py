import pymysql
from constantes import *

db = pymysql.connect(host = "localhost",
                    user = "root",
                    passwd = contraseña_base,
                    database = data_base)

cursor = db.cursor()

def ingresar_libro_en_la_base(libro):

    tupla = (
        libro.nombre,
        libro.autor,
        libro.año,
        libro.cantidad_paginas
    )

    sql = "INSERT INTO libros (nombre_libro, autor, año_libro, cantidad_paginas_libro) VALUES {};".format(tupla)

    cursor.execute(sql)
    db.commit()

    return "El libro fue insertado correctamente en el sistema"

def ingresar_cliente_en_la_base(cliente):
    
    tupla = (
        cliente.nombre,
        cliente.apellido,
        cliente.dni,
        cliente.direccion
    )

    sql = "INSERT INTO clientes (nombre_cliente, apellido_cliente, dni_cliente, direccion) VALUES {};".format(tupla)

    cursor.execute(sql)
    db.commit()

    return "El cliente fue insertado correctamente en el sistema"


def insertar_asginacion_en_la_base(asignacion):
    
    tupla = (
        asignacion.fecha,
        asignacion.id_libro,
        asignacion.id_cliente
    )

    sql = "INSERT INTO asignaciones (fecha, libro_idlibro, cliente_idcliente) VALUES {}".format(tupla)
    cursor.execute(sql)
    db.commit()

    sql = "UPDATE libros SET disponibilidad_libro = 1 WHERE idlibro = {}".format(asignacion.id_libro)
    cursor.execute(sql)
    db.commit()

    return "La asignacion fue insertada correctamente"

def mostrar_clientes():

    sql = "SELECT idcliente, nombre_cliente, apellido_cliente FROM clientes"
    cursor.execute(sql)
    lista_clientes_mostrar = cursor.fetchall()

    return lista_clientes_mostrar

def mostrar_libros():

    sql = "SELECT idlibro, nombre_libro FROM libros"
    cursor.execute(sql)
    lista_libros_mostrar = cursor.fetchall()

    return lista_libros_mostrar

def mostrar_libros_disponibles():

    sql = "SELECT * FROM libros WHERE disponibilidad_libro = 0"
    cursor.execute(sql)
    libros_disponibles = cursor.fetchall()

    return libros_disponibles

def mostrar_libros_de_un_cliente(idcliente):

    sql = """SELECT l.nombre_libro, c.nombre_cliente
    FROM libros l, clientes c
    WHERE l.idlibro = (
        SELECT  a.libro_idlibro
        FROM asignaciones a
        WHERE a.cliente_idcliente = {})
    AND c.idcliente = {};""".format(idcliente, idcliente)

    cursor.execute(sql)
    datos_asignacion = cursor.fetchall()

    return datos_asignacion

def mostrar_quien_tiene_un_libro(idlibro):
    
    sql = """SELECT c.nombre_cliente
    FROM clientes c
    WHERE idcliente = (
        SELECT a.cliente_idcliente
        FROM asignaciones a
        WHERE a.libro_idlibro = {})""".format(idlibro)

    cursor.execute(sql)
    nombre_cliente = cursor.fetchone()

    return nombre_cliente[0]

def eliminar_asignaciones():

    sql = "DELETE FROM asignaciones"
    cursor.execute(sql)
    db.commit()

def eliminar_libros():
    
    sql = "DELETE FROM libros"
    cursor.execute(sql)
    db.commit()

def eliminar_clientes():

    sql = "DELETE FROM clientes"
    cursor.execute(sql)
    db.commit()