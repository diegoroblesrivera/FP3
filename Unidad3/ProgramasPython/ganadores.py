import csv
import json
ganadores = []
with open('listadoRun.csv', 'r') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    for fila in lector_csv:
        run = fila['run']
        nombre = fila['nombre']
        # Extraer los dos últimos dígitos antes del guion
        ultimos_digitos = int(run[-4:-2])

        # Verificar si son ganadores
        if ultimos_digitos in {50, 42, 10}:
            print(f"{nombre} con RUN {run} es ganador.")
            ganadores.append(run)
        else:
            print(f"{nombre} con RUN {run} no es ganador.")
with open('ganadores.json', 'w') as archivo_json:
    json.dump(ganadores, archivo_json, indent=1)
print("Los RUN ganadores se han guardado en 'ganadores.json'.")