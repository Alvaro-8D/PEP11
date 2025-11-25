from os import strerror
import json

try:
    with open("paises.json", "r") as fichero_json:
        datos = json.load(fichero_json)
        continente = input("Dime un Continente: ")
        for fila in datos:
            if continente == fila["continente"]:
                print(f"{fila["nombre"]} está en {fila["continente"]} y tiene {fila["poblacion"]} millones de habitantes.")

except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)