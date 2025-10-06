# Escribe un programa para jugar a una versión muy simplificada del black jack. En primer
# lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (esta será su jugada). A
# continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando
# para obtener su puntuación, hasta que el quiera. Si se pasa de 21 pierde, si obtiene una
# puntuación igual o menor que la banca pierde, y si obtiene una puntuación superior a la
# banca gana.


import random

ordenador = random.randint(17, 21)
n = 0
j = -1 
jugador = 0
while j != 1:
    n = random.randint(1, 5)
    print(f"Has sacado un {n}\n")
    jugador += n
    print (f"Llevas {jugador}, no te pases de 21")
    if jugador > 21:
        print("Te has pasado de 21")
        j = 1
    else:
        j = int (input("Quieres otra carta? NO(1) Si(cualquier número)"))

if jugador <= ordenador or j == 1:
    print(f"Has perdido, mi puntuación era de {ordenador}")
else:
    print(f"Ganaste, mi puntuación era de {ordenador}")
