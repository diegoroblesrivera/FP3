import csv
import json
#Lista que guarda registros
mayores = []

with open('datos.csv', 'r') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)

    # Recorremos cada fila con un bucle for
    for fila in lector_csv:
        nombre = fila['Nombre']
        edad = int(fila['Edad'])
        comuna = fila['Comuna']
        estado_edad = "Mayor de Edad" if edad >= 18 else "Menor de Edad"
        
        print(f"{nombre} tiene {edad} años, es {estado_edad} y vive en {comuna}")

        # validamos si son mayores o iguales a 25
        if edad >= 25:
            mayores.append({
                'Nombre': nombre,
                'Edad': edad,
                'Comuna': comuna
            })
# Guardar archivo y agregar identación
with open('mayores', 'w') as archivo_json:
    json.dump(mayores, archivo_json, indent=1)

