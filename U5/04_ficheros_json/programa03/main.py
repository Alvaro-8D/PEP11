from os import strerror
import json

cadena_json = '''
[
{"nombre": "Chile", "moneda": "Peso chileno"},
{"nombre": "Egipto", "moneda": "Libra egipcia"}
]
'''

try:
    objeto_json = json.loads(cadena_json)
    print(type(objeto_json))
    for fila in objeto_json:
        print(f"{fila["nombre"]} usa '{fila["moneda"]}' como moneda")

except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)