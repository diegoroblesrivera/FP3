def primerwhile():
 text=""

 while text !="hi":
    print("Ingrese el saludo correcto")
    text=input()
 print("Ese es el saludo correcto")


def verifpassw():
 passw=""
 print("Ingrese su password ")
 passw=input()
 while passw !="1234":
    print("Su password es incorrecta")
    passw=input()
 
 print("Bienvenido Usuario Admin")

print("---Bienvenido al programa 1.0---")
print("1.- Verifica Password")
print("2.- Programa de")
op=int(input("Seleccione un a opcion"))
match op:
  case 1:
    verifpassw()
  case 2:
    primerwhile()

