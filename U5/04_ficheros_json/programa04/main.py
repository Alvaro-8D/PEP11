from os import strerror
import json

pais = {
"nombre": "Islandia",
"capital": "Reikiavik",
"idiomas": ["Islandés", "Inglés"],
"superficie_km2": 103000
}

try:
    dicionario_json = json.dumps(pais, indent=2, sort_keys=True)
    print(dicionario_json)

except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)