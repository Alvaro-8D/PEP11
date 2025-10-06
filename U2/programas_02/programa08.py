# Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación
# genera un número aleatorio entre 1 y 20. A continuación va pidiendo números y va
# respondiendo si el número a adivinar es mayor o menor que el introducido. El programa
# termina cuando se acierta el número.
# Mejora el programa de forma que el usuario tenga solo 3 intentos.

import random
# random.randint(1, 20)

secreto = random.randint(1, 20)
vidas = 3 # (intentos) jejeje

print("Puedes adivinar mi número entre 1 y 20 ???\nTienes 3 vidas\nMucha suerte JEJEJE")

for i in range(vidas):
    num = int(input(f"Intento {i+1}: "))
    if num == secreto:
        print("Enhorabuena, has sobrevivido !!!")
        break
    elif num < secreto:
        print("El número secreto es mayor  >:D")
    else:
        print("El número secreto es menor  >:D")
else:
    print(f"FALLASTE, El número era {secreto}, más suerte la próxima")

