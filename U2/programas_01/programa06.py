# Escribe un programa que pida una fecha (día, mes y anno) y diga si es correcta.

dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
anno = int(input("Introduce el anno: "))

ok = True

if mes < 1 or mes > 12:
    ok = False
elif dia < 1:
    ok = False
elif mes in [1, 3, 5, 7, 8, 10, 12] and dia > 31:
    ok = False
elif mes in [4, 6, 9, 11] and dia > 30:
    ok = False
elif mes == 2:
    if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
        if dia > 29:
            ok = False
    else:
        if dia > 28:
            ok = False

if ok:
    print("Fecha CORRECTA")
else:
    print("Fecha INCORRECTA")