from os import strerror
import json

planetas =[ {"nombre": "Marte","tipo": "rocaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaoso","lunas": 2},
            {"nombre": "Jupiter","tipo": "gaseoso","lunas": 79},
            {"nombre": "Venus","tipo": "rocoso","lunas": 0}]

try:
    with open("./RA5/planetas.json", "w") as fichero_json:
        json.dump(planetas, fichero_json,ensure_ascii=False, indent=4)

    with open("planetas.json", "r") as fichero_json:    
        dicionario_json = json.load(fichero_json)
        print(dicionario_json)

except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)

