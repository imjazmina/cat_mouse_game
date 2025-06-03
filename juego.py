import random
from tablero import Tablero
from jugador import Jugador
from algoritmo import generar_movimientos, minimax

class Juego:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.intentos = tamaño*2
        self.tablero = Tablero(tamaño)
        self.raton = Jugador("Ratón", "🐭", (tamaño//2,tamaño//2))
        self.gato = Jugador("Gato", "🐈", (0, 0))
        self.profundidad = self.intentos
        self.turno = 1

    def jugar_turno(self):
        print(f"Turno: {self.turno}, Intentos restantes: {self.intentos}")
        self.tablero.colocar(*self.raton.posicion, self.raton.simbolo)
        self.tablero.colocar(*self.gato.posicion, self.gato.simbolo)
        self.tablero.imprimir()
        self.tablero.limpiar(*self.raton.posicion)
        self.tablero.limpiar(*self.gato.posicion)

        if self.turno == 1:
            self.gato.mover(random.choice(generar_movimientos(self.gato.posicion, self.tamaño)))
            self.raton.mover(random.choice(generar_movimientos(self.raton.posicion, self.tamaño)))
        else:
            _, nueva_pos_raton = minimax(tuple(self.raton.posicion), tuple(self.gato.posicion),
                                         self.tamaño, self.profundidad, float('-inf'), float('inf'), True)
            self.raton.mover(nueva_pos_raton)

            _, nueva_pos_gato = minimax(tuple(self.raton.posicion), tuple(self.gato.posicion),
                                        self.tamaño, self.profundidad, float('-inf'), float('inf'), False)
            self.gato.mover(nueva_pos_gato)

        self.turno += 1
        self.intentos -= 1

    def estado_juego(self):
        if self.raton.posicion == self.gato.posicion:
            return True, "El gato atrapó al ratón. 🐈🐭"
        elif self.intentos == 0:
            return True, "Se han acabado los intentos.El raton ha espacapado"
        return False, ""
