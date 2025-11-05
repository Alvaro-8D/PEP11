import random
from batalla import jugador as j,enemigo as e

print("=== BATALLA DE MAGIA ===")

nombreJugador = input("Introduce tu nombre: ")
try:
    conocomientoJugador = int (input("Nivel de conocimiento (1-10):"))
    energiaJugador = int (input("Energia Inicial (1-5): "))
except Exception: #asigna puntuacion aletoria si ocurre error
    print("Error al introducir conocimiento  y/o energia inicial")
    print("Generando datos aleatorios .....")
    conocomientoJugador = random.randint(1,10)
    energiaJugador = random.randint(1,5)
    print(f"Nivel de conocimiento (1-10): {conocomientoJugador}\nEnergia Inicial (1-5): {energiaJugador}")

enemigoNombre , enemigoConocimiento , enemigoEnergia = e.generar_enemigo()

for i in range(1,4):
    j.mostrar_jugador(nombreJugador,conocomientoJugador,energiaJugador)
    e.mostrar_enemigo(enemigoNombre , enemigoConocimiento , enemigoEnergia)
    print(f"--- RONDA {i} ---")

    if (j.ataque_jugador(conocomientoJugador,energiaJugador)) > (e.ataque_enemigo(enemigoConocimiento , enemigoEnergia)):
        enemigoEnergia -= 1
        print("GANA el turno el JUGADOR")
    elif(j.ataque_jugador(conocomientoJugador,energiaJugador) == e.ataque_enemigo(enemigoConocimiento , enemigoEnergia)):
        print("EMPATE")
    else:
        energiaJugador -= 1
        print("GANA el turno el ENMEIGO")

print("=== FIN DEL DUELO ===")
if energiaJugador > enemigoEnergia:
    print(f"¡{nombreJugador} a le ha dado una paliza a {enemigoNombre}!")
elif(j.ataque_jugador(conocomientoJugador,energiaJugador) == e.ataque_enemigo(enemigoConocimiento , enemigoEnergia)):
    print(f"{nombreJugador} y el enemigo {enemigoNombre} han desistido por cansancio, ¡son igual de fuertes!")
else:
    print(f"¡{enemigoNombre} a le ha dado una paliza a {nombreJugador}!")