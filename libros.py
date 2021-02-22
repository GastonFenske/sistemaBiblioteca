
class Libro:

    def __init__(self, nombre, autor, año, cantidad_paginas):
        self.nombre = nombre
        self.autor = autor
        self.año = año
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return """
Nombre del libro:                       {}
Autor del libro:                        {}      
Año del libro:                          {}
Cantidad de paginas del libro:          {}
        """.format(self.nombre, self.autor, self.año, self.cantidad_paginas)