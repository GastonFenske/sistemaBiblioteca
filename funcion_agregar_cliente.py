from clientes import Cliente
import funciones_sql

def agregar_cliente_a_la_base(nombre, apellido, dni, direccion):
    cliente = Cliente(nombre, apellido, dni, direccion)
    funciones_sql.ingresar_cliente_en_la_base(cliente)

def datos_para_agregar_cliente():
    nombre = str(input('Ingrese el nombre del cliente: '))
    apellido = str(input('Ingrese el apellido del cliente: '))
    dni = int(input('Ingrese el dni del cliente: '))
    direccion = str(input('Ingrese la direccion del cliente: '))

    agregar_cliente_a_la_base(nombre, apellido, dni, direccion)