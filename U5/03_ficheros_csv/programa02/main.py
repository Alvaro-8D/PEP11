from os import strerror
import csv
try:
    with open("capitales.csv", mode="w") as fichero_csv:
        reader = csv.DictReader(fichero_csv, delimiter=",")
        cabeceras = reader.fieldnames
        print(f"Los nombres de las columnas son {cabeceras}")
        for fila in reader:
            print(f"El videojuego {fila[cabeceras[0]]} es del género{fila[cabeceras[1]]} y se publicó en el año {fila[cabeceras[2]]}.")
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)