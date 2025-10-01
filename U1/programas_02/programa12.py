# Sabiendo que 1 milla equivale a 1,61 Km escribe un programa que pida un número de
# millas y un número de Km, y los convierta. Resultados redondeados a 2 decimales.

millas = float(input("Introduce millas: "))
km = float(input("Introduce kilómetros: "))
print(f"{millas} millas = {millas*1.61:.2f} km")
print(f"{km} km = {km/1.61:.2f} millas")
