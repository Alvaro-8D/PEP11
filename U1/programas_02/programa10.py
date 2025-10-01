# Escribe un programa que dado un número de dos cifras, diseñe un algoritmo que permita
# obtener el número invertido.

num = int(input("Número de dos cifras: "))
invertido = (num % 10) * 10 + (num // 10)
print(f"Número invertido: {invertido}")