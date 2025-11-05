import random

def generar_enemigo():
    nombres = ["Duende","Montapuercos","Mini P.E.K.K.A","Megacaballero","Valquiria"]
    nombre = random.choice(nombres)
    conocimiento = random.randint(1,10)
    energia = random.randint(1,5)
    return nombre,conocimiento,energia

def ataque_enemigo(conocimiento, energia):
    nivelMagia = conocimiento*energia*random.randint(1,3)
    return nivelMagia

def mostrar_enemigo(nombre, conocimiento, energia):
    print(f"Nombre: {nombre} | Conocimiento: {conocimiento} | Energia: {energia}")