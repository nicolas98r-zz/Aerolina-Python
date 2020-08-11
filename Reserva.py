class Reserva:

    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def get_nombre(self):
        return self.nombre

    def get_cedula(self):
        return self.cedula