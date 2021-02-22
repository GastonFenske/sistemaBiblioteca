import funcion_agregar_libro
import funcion_agregar_cliente
import funcion_agregar_asignacion
import peticiones_sql

try:
    while True:
        print("\033[;36m"+"")
        op = int(input("""
[1]Para agregar un libro al catalogo
[2]Para añadir un cliente al sistema
[3]Para hacer una asignacion
[4]Para consultar los libros disponibles
[5]Para ver los libros que tiene un cliente
[6]Para ver quien tiene un determinado libro
[7]Para eliminar todas las asiganaciones
[8]Para eliminar todos los libros
[9]Para elimianar todos los clientes
[0]Para salir del sistema
>>>: """))
        if op == 1:
            #agregar libro al catalogo
            funcion_agregar_libro.datos_para_agregar_libro()
        elif op == 2:
            #añadir cliente al sistema
            funcion_agregar_cliente.datos_para_agregar_cliente()
        elif op == 3:
            #hacer una asignacion
            funcion_agregar_asignacion.datos_para_agregar_asignacion()
        elif op == 4:
            peticiones_sql.consultar_todos_los_libros_disponibles()
        elif op == 5:
            peticiones_sql.consultar_libros_de_un_cliente()
        elif op == 6:
            peticiones_sql.consultar_un_determinado_libro()
        elif op == 7:
            peticiones_sql.eliminar_las_asginaciones()
        elif op == 8:
            peticiones_sql.eliminar_todos_los_libros()
        elif op == 9:
            peticiones_sql.eliminar_todos_los_clientes()
        elif op == 0:
            print('Ha abandonado el sistema...')
            break
        else:
            print('Esa opcion no corresponde a nada')
except ValueError:
    print('Ingresa bien las opciones capo')