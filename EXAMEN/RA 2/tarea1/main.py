import random
# random.randint(1, 6)

vidaJugador = 3
puntos = 0

while vidaJugador > 0:
    print(f"Vidas: {vidaJugador}")
    tipoAtaque = 0
    while not((tipoAtaque == 1)or(tipoAtaque == 2)or(tipoAtaque == 3)):
        try:
            tipoAtaque = int (input("1.Fuerza  2.Precision  3.Riesgo: "))
            if not((tipoAtaque == 1)or(tipoAtaque == 2)or(tipoAtaque == 3)):
                print("Debes introducir un tipo de ataque correcto (1, 2 o 3)")
        except Exception:
            print("Debes introducir un tipo de ataque correcto (1, 2 o 3)")
    match tipoAtaque:
        case 1:
            tipoAtaque = random.randint(5, 10)
            defensaEnemigo = random.randint(3, 10)
        case 2:
            tipoAtaque = random.randint(3, 8)
            defensaEnemigo = random.randint(2, 9)
        case 3:
            tipoAtaque = random.randint(1, 10)
            defensaEnemigo = random.randint(1, 8)
        case _:
            print("Error")
    if tipoAtaque > defensaEnemigo:
        puntos += 1
        print("Has GANDADO el turno")
    elif tipoAtaque == defensaEnemigo:
        print("EMPATE")
    else:
        vidaJugador -= 1
        print("Has PERDIDO el turno")

print(f" * * * * GAME OVER: {puntos} puntos * * * * ")
