# Escribe un programa que reciba una cantidad de minutos y muestre por pantalla a
# cuantas horas y minutos corresponde.

minutos = int(input("Introduce minutos: "))
horas = minutos // 60
resto = minutos % 60
print(f"{minutos} minutos = {horas} horas y {resto} minutos")