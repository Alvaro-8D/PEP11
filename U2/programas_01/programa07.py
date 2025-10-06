# Escriba un programa que pida un año y que escriba si es bisiesto o no. Un año es bisiesto
# si es múltiplos de 4 pero no múltiplos de 100, aunque si los múltiplos de 400.

anno = int(input("Introduce el anno: "))

ok = True

if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
    ok= False

if ok:
    print("Año BISIESTO")
else:
    print("Año NOOOO BISIESTO")