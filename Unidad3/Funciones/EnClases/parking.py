from datetime import datetime
parking=[
    [[],[],[],[],[],[],[],[],[],[],[],[],[],
    [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]], #piso 1
    [[],[],[],[],[],[],[],[],[],[],[],[],[],
    [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]], #piso 2
    [[],[],[],[],[],[],[],[],[],[],[],[],[],
    [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]], #piso 3
]
entra=datetime.now()
parking[2][2]={"placa":"placa", "fecha": entra}

print(parking[2][2]["fecha"].strftime("%H:%M"))

def calcula_tiempo(piso, sitio, placa):
    diferencia = datetime.now() - parking[piso-1][sitio-1]["fecha"]
    return diferencia
def ingresa(piso, sitio, placa):
    entra=datetime.now()
    parking[piso-1][sitio-1]={"placa":placa, "fecha": entra}


while True:
    print("Bienvenido ")
    print("""
 //Que desea hacer?//
    1)Ingresar un vehiculo
    2)Verificar el tiempo de un vehiculo
    3)Cobrar servicio
    4)Guardar en un Archivo
    5)Salir
    """)
    op=int(input("SELECCIONE UNA OPCION\n"))
    match op:
        case 1:
            piso=int(input("Ingrese un piso\n"))
            piso=int(input("Ingrese un piso\n"))



