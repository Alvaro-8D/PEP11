import random

def ataque_jugador(conocimiento, energia):
    return conocimiento*energia*random.randint(1,3)

def mostrar_jugador(nombre, conocimiento, energia):
    print(f"Nombre: {nombre} | Conocimiento: {conocimiento} | Energia: {energia}")