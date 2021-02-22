

class Cliente:

    def __init__(self, nombre, apellido, dni, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion

    def __str__(self):
        return """
Nombre del cliente:         {}
Apellido del cliente:       {}
Dni del cliente:            {}
Direccion del cliente:      {}
        """.format(self.nombre, self.apellido, self.dni, self.direccion)