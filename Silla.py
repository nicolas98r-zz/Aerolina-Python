class Silla:

    def __init__(self, fila, letra):
        self.fila = fila
        self.letra = letra
        self.reserva = None

    def get_fila(self):
        return self.fila

    def get_letra(self):
        return self.letra

    def esta_reservada(self):
        return self.reserva

    def reservar(self, reserva):
        self.reserva = reserva

    def to_string(self):
        return ("" + str(self.fila) + self.letra)