# Escribe un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

f = float(input("Introduce grados Fahrenheit: "))
c = (f - 32) * 5/9
print(f"{f}°F = {c:.2f}°C")