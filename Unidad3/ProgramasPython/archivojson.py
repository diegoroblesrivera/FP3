import json

# Datos JSON
datos = {
    "nombre": "Esteban",
    "edad": 29,
    "comuna": "La Granja",
    "estudios": ["colegio Arturo Prat", "liceo el bosque",
                 "Duoc UC", "Diplomado Duoc UC"]
    
}

# Abre el archivo, w es permiso de escritura
with open('archivo24.json', 'w') as archivo:
    json.dump(datos, archivo)



# import json

# # Abrir archivo, r es permiso de lectura
# with open('archivo.json', 'r') as archivo:
#     datos_leidos = json.load(archivo)
# print(datos_leidos)
