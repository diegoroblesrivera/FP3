stay=True
gasto=0
nombre=""
while stay:
 print("--Bienvenido Usuario--")
 print("Seleccione una opcion")
 print("1.- Ingrese su nombre")
 print("2.- Ingrese su gasto")
 print("3.- Ver resultados")
 print("4.- Salir")
 op=int(input())

 match op:
     case 1:
         nombre=input()
         print("Nombre ingresado con exito")
     case 2:
         gasto=gasto+int(input())
         print("Opcion 2")
     case 3:
         print("Hola ", nombre, "su gasto es ", gasto )
     case 4:
       stay=False
     case _:
         print("Elija una opcion valida")