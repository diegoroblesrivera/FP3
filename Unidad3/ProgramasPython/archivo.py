import csv

# Sintaxis: open('nombre_del_archivo.csv', 'modo', newline='')
# Modo común: 'w' (escritura)
with open('nuevo_archivo.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    
    # Escribir una fila en el archivo CSV
    escritor_csv.writerow(['Nombre', 'Edad', 'Ciudad'])
    
    # Escribir múltiples filas en el archivo CSV
    escritor_csv.writerows([
        ['Juan', 25, 'Lima'],
        ['María', 30, 'Bogotá'],
        ['Carlos', 22, 'Madrid']
    ])
