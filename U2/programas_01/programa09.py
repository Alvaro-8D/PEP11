# Escribe un programa en Python que simule el juego de piedra, papel o tijera. En primer
# lugar el programa tendrá que mostrar un mensaje por pantalla al usuario para preguntarle
# qué opción desea elegir. Por ejemplo:
# 1. Piedra
# 2. Papel
# 3. Tijera
# Seleccione una opción (1, 2 o 3):
# Después de leer la opción seleccionada por el usuario el programa generará un número
# aleatorio para simular una jugada y mostrará un mensaje indicando si el usuario ha
# ganado o ha perdido dependiendo del resultado.
# Ten en cuenta que:
# • La piedra gana a la tijera pero pierde contra el papel.
# • El papel gana a la piedra pero pierde contra la tijera.
# • La tijera gana al papel pero pierde contra la piedra.

import random
# random.randint(1, 3)

num1 = int (input("Qué opción eliges: \n+ Piedra(1)\n+ Papel(2)\n+ Tijeras(3)\n"))

match num1:
    case 1:
        print("Elejiste Piedra")
        
    case 2:
        print("Elejiste Papel")
    
    case 3:
        print("Elejiste Tijeras")
        
    case _:
        print("Opción no válida")

num2 = random.randint(1, 3)

match num2:
    case 1:
        print("RoBot eligió Piedra")
        
    case 2:
        print("RoBot eligió Papel")
    
    case 3:
        print("RoBot eligió Tijeras")
        
    case _:
        print("Opción no válida")

if num1 == num2:
    print("Empate")
else:
    if num1 == 1 and num2 == 2:
        print("Gana Jugador 2")

    elif num1 == 1 and num2 == 3:
        print("Gana Jugador 1")

    elif num1 == 2 and num2 == 1:
        print("Gana Jugador 1")

    elif num1 == 2 and num2 == 3:
        print("Gana Jugador 2")

    elif num1 == 3 and num2 == 1:
        print("Gana Jugador 2")

    elif num1 == 3 and num2 == 2:
        print("Gana Jugador 1")

    



