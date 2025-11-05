minutos = int (input("Introduce una cantidad de minutos: "))

horas = int (minutos / 60)
resto = minutos - (horas*60)

print("Equivale a "+str(horas)+" horas y "+str(resto)+" minutos")