class Tablero:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.matriz = [[' ' for _ in range(tamaño)] for _ in range(tamaño)]

    def colocar(self, x, y, simbolo):
        self.matriz[x][y] = simbolo

    def limpiar(self, x, y):
        self.matriz[x][y] = ' '

    def imprimir(self):
        for fila in self.matriz:
            print(" ".join(f"[{cel}]" for cel in fila))
        print()
