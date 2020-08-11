class Ciudad:

    def __init__(self, nombre_ciudad, coordenada_x, coordenada_y):
        self.nombre = nombre_ciudad
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.siguiente = None
        self.vuelo1 = None

    def get_x(self):
        return self.coordenada_x

    def get_y(self):
        return self.coordenada_y

    def get_vuelos(self):
        vuelos = list()
        for vuelo in self.vuelo1:
            vuelos.append(vuelo)
        return vuelos

    def añadir_vuelo(self, codigo, fecha, hora, minuto):
        nuevo_vuelo = Vuelo(codigo, fecha, hora, minuto)

        vuelo_temp1 = None
        vuelo_temp2 = self.vuelo1

        while vuelo_temp1 != None and vuelo_temp2.get_codigo() < codigo:
            vuelo_temp1 = vuelo_temp2
            vuelo_temp2 = vuelo_temp2.get_vuelo_siguiente()

        vuelo_temp1.insertar_despues(nuevo_vuelo)

    def buscar_vuelo(self, codigo):
        for vuelo in self.vuelo1:
            if vuelo.get_codigo == codigo:
                return vuelo
        return None

    def get_primer_vuelo(self):
        return self.vuelo1

    def get_siguente(self):
        return self.siguiente

    def agregar_siguiente(self, siguiente):
        self.siguiente = siguiente

