# op=int(input())

# match op:
#     case 1:
#         print("Opcion 1")
#     case 2:
#         print("Opcion 2")
#     case 3:
#         print("Opcion 3")
#     case 4:
#         print("Opcion 4")
#     case _:
#         print("Opcion por defecto")
mantener=True

while mantener:

    print("1.- Suma")
    print("2.- Resta")
    print("3.- Division")
    print("4.- Multiplicacion")
    print("5.- Salir")
    op=int(input("Ingrese un a opcion"))


    match op:
        case 1:
            print("Ingrese un numero")
            num1=int(input())
            print("Ingrese otro numero")
            num2=int(input())
            print(num1+num2)
        case 2:
            print("Ingrese un numero")
            num1=int(input())
            print("Ingrese otro numero")
            num2=int(input())
            print(num1-num2)
        case 3:
            print("Ingrese un numero")
            num1=int(input())
            print("Ingrese otro numero")
            num2=int(input())
            print(num1/num2)
        case 4:
            print("Ingrese un numero")
            num1=int(input())
            print("Ingrese otro numero")
            num2=int(input())
            print(num1*num2)
        case 5:
           mantener=False
        case _:
            print("Ingrese una opcion correcta")
        