class Jugador:
    def __init__(self, nombre, simbolo, posicion):
        self.nombre = nombre
        self.simbolo = simbolo
        self.posicion = posicion

    def mover(self, nueva_posicion):
        self.posicion = nueva_posicion
