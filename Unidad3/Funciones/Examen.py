matriz=[

    [[], [], []], #piso 1
    [[], [], []], #piso 2
    [[], [], []], #piso 3
]

def ingresar(piso, hab, name):

    matriz[piso-1][hab-1]=name
def verificar(piso,hab):
     if matriz[piso-1][hab-1]!=[]:
        return False
     else:
        return True
def mostrar():
        for i in matriz:
            print(i)
def contar_venta():
    totalventa=0
    for piso in matriz:
            for hab in piso:
                if hab != []:
                    totalventa=totalventa+ 100
    print(totalventa)
               

def guardar():
    with open("info.txt", "a") as f:
            for piso in matriz:
                for hab in piso:
                    f.write(str(hab))
                f.write('\n')


while True:
    print("""Bienvenido al hotel Transiylvania
          1.- Registrar Pasajero
          2.- Verificar hotel
          3.- Guardar Registro
          4.- Hacer Checkout
          5.- Salir
          """)
    op=int(input("Seleccione un a opcion\n"))
    match op:
        case 1:
                piso=int(input("Ingrese el piso\n"))
                while piso<1 or piso>3:
                    piso=int(input("Ingrese el piso del 1 al 3\n"))
                hab=int(input("Ingrese la habitacion\n"))
                while hab<1 or hab>3:
                    hab=int(input("Ingrese el piso del 1 al 3\n"))
                if verificar(piso,hab) ==False:
                     print("La habitacion esta opcupada")
                else:
                    name=input("ingrese nombre")
                    ingresar(piso, hab, name)
        case 2:
            mostrar()
            contar_venta()
        case 3:
            guardar()
        case 4:
                piso=int(input("Ingrese el piso\n"))
                while piso<1 or piso>3:
                    piso=int(input("Ingrese el piso del 1 al 3\n"))
                hab=int(input("Ingrese la habitacion\n"))
                while hab<1 or hab>3:
                    hab=int(input("Ingrese el piso del 1 al 3\n"))
                matriz[piso-1][hab-1]=[]
                print("La habitacion está desocupada ahora")
            
        case 5:
            print("que tenga buen dia")
            break
        case _:
            print("Seleccione una opcion válida")