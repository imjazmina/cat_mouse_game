import random
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # arriba, abajo, izquierda, der

def generar_movimientos(pos, tamaño):
    moves = []
    for dx, dy in movimientos:
        x, y = pos[0] + dx, pos[1] + dy
        if 0 <= x < tamaño and 0 <= y < tamaño:
            moves.append((x, y))
    return moves

def distancia_manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def evaluar_estado_raton(pos_gato, pos_raton):
    if pos_raton == pos_gato:
        return -1000
    return  100 * distancia_manhattan(pos_raton, pos_gato) # prioriza la salida sin acercarse al gato

def evaluar_estado_gato(pos_gato, pos_raton):
    if pos_gato == pos_raton:
        return 1000
    return -distancia_manhattan(pos_gato, pos_raton)

def minimax(pos_raton, pos_gato, tamaño, profundidad, alfa, beta, maximizador):
    if pos_raton == pos_gato:
        return (-1000 if maximizador else 1000), pos_raton

    if profundidad == 0:
        if maximizador:
            return evaluar_estado_raton(pos_gato, pos_raton), pos_raton
        else:
            return evaluar_estado_gato(pos_gato, pos_raton), pos_gato

    if maximizador:
        mejor_valor = float('-inf')
        mejor_mov = pos_raton
        for mov in generar_movimientos(pos_raton, tamaño):
            val, _ = minimax(mov, pos_gato, tamaño, profundidad - 1, alfa, beta, False)
            if val > mejor_valor:
                mejor_valor = val
                mejor_mov = mov
            alfa = max(alfa, val)
            if beta <= alfa:
                break
        return mejor_valor, mejor_mov
    else:
        mejor_valor = float('inf')
        mejor_mov = pos_gato
        for mov in generar_movimientos(pos_gato, tamaño):
            val, _ = minimax(pos_raton, mov, tamaño, profundidad - 1, alfa, beta, True)
            if val < mejor_valor:
                mejor_valor = val
                mejor_mov = mov
            beta = min(beta, val)
            if beta <= alfa:
                break
        return mejor_valor, mejor_mov
