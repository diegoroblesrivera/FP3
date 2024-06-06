import csv
import json
with open('listadoRutEmpresa.csv', 'r') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    empresas = list(lector_csv)
for empresa in empresas:
    ventas = int(empresa['ventas'])
    if ventas < 100000000:
        empresa['clasificacionEmpresa'] = 'Pequeño Contribuyente'
    elif 100000000 < ventas <= 200000000:
        empresa['clasificacionEmpresa'] = 'Mediano Contribuyente'
    else:
        empresa['clasificacionEmpresa'] = 'Gran Contribuyente'

with open('segmentacionEmpresas.json', 'w') as archivo_json:
    json.dump(empresas, archivo_json, indent=1)
