def primerwhile():
 text=""

 while text !="hi":
    print("Ingrese el saludo correcto")
    text=input()
 print("Ese es el saludo correcto")

# primerwhile()

def verifpassw():
 passw=""
 print("Ingrese su password ")
 passw=input()
 while passw !="1234":
    print("Su password es incorrecta")
    passw=input()
 
 print("Bienvenido Usuario Admin")

verifpassw()