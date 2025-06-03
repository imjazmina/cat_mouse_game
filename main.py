from juego import Juego

if __name__ == "__main__":
    print("Bienvenido al juego del Gato y el Ratón 🐭🐈🚪")
    juego = Juego(tamaño=5)

    while True:
        juego.jugar_turno()
        terminado, mensaje = juego.estado_juego()
        if terminado:
            print(mensaje)
            break
