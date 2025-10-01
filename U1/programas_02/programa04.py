# Escribe un programa que pregunte la base y altura de un rectángulo y calcule su área y perímetro.

base = float(input("Introduce la base: "))
altura = float(input("Introduce la altura: "))
area = base * altura
perimetro = 2 * (base + altura)
print(f"Área: {area}, Perímetro: {perimetro}")