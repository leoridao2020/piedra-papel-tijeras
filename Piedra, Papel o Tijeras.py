import random

def jugar_ppt():
    opciones = ["piedra", "papel", "tijera"]

    # Elección del jugador
    eleccion_jugador = input("Elige piedra, papel o tijera: ")

    # Elección de la computadora
    eleccion_computadora = random.choice(opciones)

    print("La computadora eligió:", eleccion_computadora)

    # Verificar ganador
    if eleccion_jugador == eleccion_computadora:
        print("Es un empate!")
    elif (eleccion_jugador == "piedra" and eleccion_computadora == "tijera") or \
            (eleccion_jugador == "papel" and eleccion_computadora == "piedra") or \
            (eleccion_jugador == "tijera" and eleccion_computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("Perdiste.")

# Ejecutar el juego
jugar_ppt()
