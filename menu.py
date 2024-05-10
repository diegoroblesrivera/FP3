def suma():
   num1=int(input())
   num2=int(input())
   result=num1+num2
   return result



stay=True
gasto=0
while stay:
 print("--Binvenido al sistema Python--")
 print("Seleccione una opcion")
 print("1.- Escriba su nombre")
 print("2.- Ingrese su gasto")
 print("3.- Ingrese su año de nacimiento")
 print("4.- Vea Resultados")
 print("5.- Salir")
 opcion=int(input())
 
 match opcion:
     case 1:
         nombre=input()
     case 2:
         gasto=gasto+int(input())
     case 3:
        nac=int(input())
     case 4:
          print("Hola ",nombre,  "y su edad es ",str(2024-nac) ,   "Usted ha gastado" , gasto)
     case 5:
         stay=False
     case _:
        print("Usted ha elegido una Opcion invalida")