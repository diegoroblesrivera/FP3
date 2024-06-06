import csv

# Sintaxis: open('nombre_del_archivo.csv', 'modo', newline='')
# Modo común: 'w' (escritura)
with open('nuevo_archivo.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    
    # Escribir una fila en el archivo CSV
    escritor_csv.writerow(['Nombre', 'Edad', 'Comuna'])
    
    # Escribir múltiples filas en el archivo CSV
    escritor_csv.writerows([
        ['Esteban', 25, 'Santiago'],
        ['María', 30, 'Valparaíso'],
        ['Carlos', 22, 'Osorno'],
        ['Sigrid', 25, 'Santiago'],
        ['Daniela', 30, 'La Cisterna'],
        ['Aylen', 22, 'La florida']
    ])

import csv
# Sintaxis: open('nombre_del_archivo.csv', 'modo', newline='')
# Modo común: 'r' (lectura)
with open('nuevo_archivo.csv', 'r', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    
    for fila in lector_csv:
        print(fila)
