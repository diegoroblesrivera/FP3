import time
print("Bienvenido al Restaurant!")
time.sleep(2)
print("A continuacion le daremos el menu...")
nombre=(input("Ingrese su nombre porfavor: "))
cuenta=0
estar=True
time.sleep(2)
print("Menu: ")
time.sleep(1)
print("1- Arroz a la francesa - $4.500")
time.sleep(1)
print("2- Arroz marinero -  $5.200")
time.sleep(1)
print("3- Sopa marinera - $9.700")
time.sleep(1)
print("4- Total de la boleta")
time.sleep(1)
print("5- Salir del Restaurant")
time.sleep(1)
while estar:
    opcion=int(input("Ingrese su opcion: "))
    match opcion:
        case 1:
            print("Don", nombre)
            time.sleep(1)
            print("Usted a elegido arroz a la francesa!")
            time.sleep(1)
            print("Precio : $4.500")
            cuenta=cuenta+4500
            
        case 2:
            print("Don", nombre)
            print("Usted a elegido Arroz Marinero!")
            time.sleep(2)
            print("Precio $5.200")
            cuenta=cuenta+5200
        case 3:
            print("Don", nombre)
            print("Usted a elegido Sopa Marinera - $9.700")
            time.sleep(2)
            print("Precio $9.700")
            cuenta=cuenta+9700
        case 4:
            print("El total de su boleta es: ", cuenta)
        case 5:
            print("Gracias por usar el progama!")
            estar=False
        case _:
            print("Opcion Invalida.")