# Modifica el programa anterior para que pida en primer lugar el número de jugadores que
# van a jugar. Cada jugador irá jugando y el programa mostrará si ha ganado o no a la
# banca.


import random
players = int (input("Cuantos jugadores van a jugar ??? >:)\n"))

for p in range(1,players+1):
    ordenador = random.randint(17, 21)
    n = 0
    j = -1 
    jugador = 0
    cagada = False # Si se pasa de 21
    while j != 1:
        n = random.randint(1, 5)
        print(f"Has sacado un {n}\n")
        jugador += n
        print (f"Llevas {jugador}, no te pases de 21")
        if jugador > 21:
            print("Te has pasado de 21")
            j = 1
            cagada = True
        else:
            j = int (input("Quieres otra carta? NO(1) Si(cualquier número)"))

    print(">--------------------------------------------------------------<") #para que se vea mejor 
    if jugador <= ordenador or cagada:
        print(f"Jugador[{p}] ha PERDIDO con {jugador}, mi puntuación era de {ordenador}")
    else:
        print(f"Jugador[{p}] ha GANADO con {jugador}, mi puntuación era de {ordenador}")
    print(">--------------------------------------------------------------<\n") #para que se vea mejor 




