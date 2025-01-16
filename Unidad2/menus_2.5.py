dd=100000

while True:
    print("""
          1.- Pago de Tarjeta de Crédito:
          2.- Simulación de Compras:
          3.- Salir
          """)
    op=int(input("Seleccione una opcion"))
    match op:
        case 1:
            print("Su deuda actual es de ", dd)
            pago=int(input())
            if pago<=0 or pago>dd:
                print("El pago debe ser mayor a cero y menor que la deuda")
            else:
                dd=dd-pago
            print("El saldo a pagar es ", dd)
        case 2:
            while True :
                print("""Seleccione un item
                    1.- Monitor
                    2.- Teclalo
                    3.- Laptop
                    4.Salir
                    """)
                ops=int(input())
                match ops:
                    case 1:
                       valor=80000
                       dd=valor+dd
                       print("Usted añadió un nuevo articulo, su nuevo saldo es ", dd)
                    case 2:
                        valor=50000
                        dd=valor+dd
                        print("Usted añadió un nuevo articulo, su nuevo saldo es ", dd)
                    case 3:
                        valor=1180000
                        dd=valor+dd
                        print("Usted añadió un nuevo articulo, su nuevo saldo es ", dd)
                    case 4:
                        print("Gracias por su compra")
                        break
                    case _:
                        print("Seleccione una opcion válida 1-3")
        case 3:
            print("Gracias por usar el sistema de Crédito")
            break
        case _:
            print("Seleccione una opcion válida 1-3")
    