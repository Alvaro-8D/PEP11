from os import strerror
import csv

cabeceras = ["Ciudad", "País", "Lugar emblemático"]

datos = [
{"Ciudad": "Roma", "País": "Italia", "Lugar emblemático": "Coliseo"},
{"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
{"Ciudad": "Kioto", "País": "Japón", "Lugar emblemático": "Templos históricos"}
]

try:
    with open("patrimonios.csv","w") as fichero_csv:
        writer = csv.DictWriter(fichero_csv)
        writer.writeheader(cabeceras,";")
        writer.writerows("hola",";")
        print("Archivo 'capitales.csv' creado correctamente.")

except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)