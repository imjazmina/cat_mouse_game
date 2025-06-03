# 🐭 El Gato y el Ratón - Simulación con Minimax

Este proyecto es una simulación por consola de un juego entre un **ratón que intenta escapar** y un **gato que intenta atraparlo**, utilizando el algoritmo **Minimax con poda alfa-beta** para tomar decisiones inteligentes.

---

## 🎯 Objetivo del Juego

- El **gato** intentará alcanzar al ratón y este lo esquivara de el durante los turnos. 
- El juego se desarrolla en una **rejilla de N x N casillas**.

---

## 🧠 Inteligencia Artificial

Se utiliza el algoritmo **Minimax con poda alfa-beta** para:

- Evaluar las posibles jugadas del **ratón**, priorizando alejarse del gato.
- Evaluar las jugadas del **gato**, buscando reducir la distancia hasta el ratón.

La IA considera:

- Posiciones válidas (sin salirse del tablero).
- Distancia de Manhattan para calcular cercanía entre el gato y el ratón.
- Profundidad limitada para evitar cálculos infinitos.

---

## 🛠️ Estructura del Código

### Funciones principales:

| Función                        | Descripción                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| `d_manhattan(p1, p2)`         | Calcula la distancia Manhattan entre dos posiciones.                        |
| `evaluar_estado_raton(...)`   | Evalúa un estado para el ratón. Prioriza alejarse del gato.                 |
| `evaluar_estado_gato(...)`    | Evalúa un estado para el gato.                                             |
| `estado_juego(...)`           | Determina si el juego terminó (ratón atrapado o sin intentos).             |
| `minimax(...)`                | Aplica minimax para decidir la mejor jugada de ambos jugadores              |

