# ---------------Clase Vuelo ------------
# Diego Alejandro Tellez - 20162020015
# Edwin Alejandro Fiesco - 20182020108
# Nicolas Ramírez Manrique – 20162020033
class Vuelo:
    def __init__(self, fecha, hora, minutos, ID, lugar_partida, lugar_destino):
        self.capacidad = 16 * 6
        self.sillas_disponibles = self.capacidad
        self.sillas = [15][6]
        self.horario = str(fecha)+"/"+str(hora)+"/"+str(minutos)
        self.id = ID
        self.lugar_partida = lugar_partida
        self.lugar_destino = lugar_destino

    def asignar_silla(self, fila, columna, cedula):
        if self.sillas_disponibles != 0:
            if not (self.sillas[fila][columna].is_reservada() or self.sillas[fila][columna].is_ocupada()):
                self.sillas[fila][columna].set_ocupada(cedula)
                self.sillas_disponibles -= 1
                return True
            else:
                return False

    def reservar_silla(self, fila, columna, cedula):
        if self.sillas_disponibles != 0:
            if not (self.sillas[fila][columna].is_reservada() or self.sillas[fila][columna].is_ocupada()):
                self.sillas[fila][columna].set_reservada(cedula)
                self.sillas_disponibles -= 1
                return True
            else:
                return False

    def get_ruta(self):
        return self.lugar_partida, self.lugar_destino

    def cancelar_reservacion(self, fila, columna):
        self.sillas[fila][columna].set_reservada(None)
        self.sillas[fila][columna].set_ocupada(None)

    def get_ID(self):
        return self.id

    def get_horario(self):
        return self.horario

    def get_sillas_disponibles(self):
        return self.sillas_disponibles

    def get_capacidad(self):
        return self.capacidad