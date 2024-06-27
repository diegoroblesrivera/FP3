economica = [
    [[], [], [], [], [], [], [], [], [], [], [], [],[],[],[],[] ],
    [[], [], [], [], [], [], [], [], [], [], [], [],[],[],[],[] ],
    [[], [], [], [], [], [], [], [], [], [], [], [],[],[],[],[] ],
]
turista = [
  [[], [], [], [], [], [], [], [], [], [], [], [],[],[],[],[] ],
  [[], [], [], [], [], [], [], [], [], [], [], [],[],[],[],[] ],
]
ejecutiva = [
    [[], [], [], [], [], [], [], [], [], [], [], [],[],[],[],[] ],
]


def resv_economica(fila, asiento, nombre, rut):
    if fila>=0 and fila<=3:
        if not economica[fila][asiento]: 
            economica[fila][asiento] = nombre,rut
            print (f"la compra fue realizada en la clase economica en la fila{fila} y el asiento{asiento}")
        else:
         print(f"Estimado/a el asiento que desea esta ocupado")
    else:
        print("porfavor ingrese una fila del 0 al 6")
def resv_turista(fila, asiento, nombre, rut):
    if fila>=0 and fila<=3:
        if not turista[fila][asiento]: 
            turista[fila][asiento] = nombre,rut
            print (f"la compra fue realizada en la clase turista en la fila{fila} y el asiento{asiento}")
        else:
         print(f"Estimado/a el asiento que desea esta ocupado")
    else:
        print("porfavor ingrese una fila del 0 al 6")
def resv_ejecutiva(fila, asiento, nombre, rut):
    if fila>=0 and fila<=3:
        if not ejecutiva[fila][asiento]: 
            economica[fila][asiento] = nombre,rut
            print (f"la compra fue realizada en la clase ejecutiva en la fila{fila} y el asiento{asiento}")
        else:
            print(f"Estimado/a el asiento que desea esta ocupado")
    else:
        ("porfavor ingrese una fila del 0 al 6")


while True:
    print("Bienvenido ")
    print("""
 //Que tipo de asiento desea?//
    1)economica
    2)turista
    3)ejecutiva
    4)mostrar compra
    """)
    op = int(input("Seleccione una opcion: "))
    match op:
        case(1):
            fila=int(input("ingrese su fila "))
            asiento=int(input("ingrese su asiento "))
            nombre=str(input("ingrese su nombre "))
            rut=str(input("ingrese su rut "))
            resv_economica(fila, asiento, nombre, rut)

        case(2):
          fila=int(input("ingrese su fila "))
          asiento=int(input("ingrese su asiento "))
          nombre=str(input("ingrese su nombre "))
          rut=str(input("ingrese su rut "))
          resv_turista(fila, asiento, nombre, rut)

        case(3):
            fila=int(input("ingrese su fila "))
            asiento=int(input("ingrese su asiento "))
            nombre=str(input("ingrese su nombre "))
            rut=str(input("ingrese su rut "))
            resv_ejecutiva(fila, asiento, nombre, rut)
            

        case(4):
            print("que clase compro ")
            print("""
            1)economica
            2)turista
            3)ejecutiva
            4)salir
                """)
            op=int(input("que clase compro"))
            match op:
                case(1):
                    for i in economica :
                        print(i)
                case(2):
                    for i in turista:
                        print(i)
                case(3):
                    for i in turista:
                        print(i)
                case(4):
                    break
        case(5):
            print()
             