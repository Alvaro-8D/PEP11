# Escribe un programa que simule un juego en el que dos jugadores tiran dos dados. El que
# saque mayor puntuación total, gana. Si la puntuación total coincide, gana quien haya
# sacado el dado con el valor más alto. Si el valor más alto también coincide, empatan.
# Puedes pedir el valor de cada tirada de dados por teclado o usar la la función
# random.randrange(1, 7) para obtener un número aleatorio entre 1 y 6 (para ello
# debes poner import random al inicio del programa)

import random
# random.randint(1, 6)

num1 = int (input("Dados manual(1) / Dados Automáticos(2): "))

match num1:
    case 1:
        print("Modo manual")
        j1a = int (input("Dado 1 Jugador 1: "))
        j1b = int (input("Dado 2 Jugador 1: "))
        j2a = int (input("Dado 1 Jugador 2: "))
        j2b = int (input("Dado 2 Jugador 2: "))
    case 2:
        print("Dados generados Automáticamente")
        j1a = random.randint(1, 6)
        j1b = random.randint(1, 6)
        j2a = random.randint(1, 6)
        j2b = random.randint(1, 6)
    case _:
        print("Opción no válida")

j1 = j1a+j1b
j2 = j2a+j2b

print("Jufador 1: "+str(j1a)+" + "+str(j1b)+" = "+str(j1))
print("Jufador 2: "+str(j2a)+" + "+str(j2b)+" = "+str(j2))

if j1 > j2:
    print("Gana Jugador 1")
else:
    if j1 == j2:
        # En caso de Empate
        
        j1 = j1a
        if j1b > j1a: j1 = j1b

        j2 = j2a
        if j2b > j2a: j2 = j2b


        if j1 > j2:
            print("Gana Jugador 1")
        else:
            if j1 == j2:
                print("Empate")    
            else:
                print("Gana Jugador 2")
    else:
        print("Gana Jugador 2")





