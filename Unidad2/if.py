# num=-7

# if num>0 :
#     print("El numero es positivo")
# else:
#     print("El numero no es positivo")

# num=7

# if num>0 and num%2==0:
#     print("El numero es positivo y par")
# else:
#     print("El numero es positivo y no es par")




# number=7
# edad=45

# if number>edad:
#     print("La variable  es verdadera.")
# elif edad > 50:
#     print("La suma es mayor que 50.")
# else:
#     print("Ninguna de las condiciones anteriores se cumple.")

# alex=15
# sam=77
# ada=60

# if alex<sam:
#     if sam>ada:
#         print("Sam es el mayor de todos ")
#     else:
#         print("Sam solo es mayor que alex" ) 


# leche_sin_lactosa=True
# caja_habilitada=True
# lider_abierto=True
# sistema_de_pago=False



# if lider_abierto:
#     print("Puede entar al super")
#     if leche_sin_lactosa:
#         print("Hay leche sin lactosa")
#         if caja_habilitada:
#             print("Hay cajas habilitadas")
#             if sistema_de_pago:
#                 print("Puede pagar con debito")
#             else:
#                 print("Puede pagar con efectivo")

# num1=19
# num2=18
# num3=31

# if num1>num2 and num1>num3:
#         print("el numero mayor es", num1)
# elif num2>num3:
#         print("el numero mayor es", num2)
# else:
#         print("el numero mayor es", num3) 


# tacos=1
# pizza=2
# humitas=3
# cazuela=4
# print("Elija una opcion de comida")
# print("""tacos=1
# pizza=2
# humitas=3
# cazuela=4""")
# op=int(input())
# if op==(1):
#         print("Usted prefiere los Tacos")
# elif(op==(2)):
#         print("Usted prefiere la pizza")
# elif(op==(3)):
#         print("Usted prefiere las humitas")
# elif(op==(4)):
#         print("Usted prefiere la cazuela")
# else:
#         print("Usted es regodion")

###ejemplo de variable boleana  ###
# ticket_valido=False

# folio_valido=123
# print("Ingrese el numero de folio")
# n_folio=int(input())

# if n_folio==folio_valido:
#         ticket_valido=True

# if ticket_valido:
#         print("este ticket és valido")
# else:
#         print("este ticket caducó")

# edad=19
# grupo="A"

# if edad>=18 and  grupo=="A":
#         print("Used es mayor y pertenece al grupo A")
# elif edad>=18 and  grupo=="B":
#         print("Used es mayor y pertenece al grupo B")
# else:
#  print("Used no es mayor y no pertenece a ningun grupo")


# color="Negro"

# if color=="Azul" or  color=="Negro" or color=="Rojo":
#         print("Usted tiene por lo menos un color")


# Validar si un ticker está dentro del rango valido
# entre 100 y 750

# Validar si va a cancha o a galeria

# print("Ingrese su numero de ticket:")
# num_ticket=int(input())

# if num_ticket > 100 and num_ticket < 750:
 
#  print("Su ticket es valido")
#  print("Donde va?")
#  print("Galeria (G) o Cancha (C)?")
#  donde=input()
#  if donde.upper() == "G":
#         print("Usted va a la galeria, Disfrute!")
#  elif donde.upper() == "C":
#             print("Usted va a la cancha")
#  else:
#                 print("No va a ningun lado")
# else:
#   print("Ticket maloo")


#calculadora

#definicion de operaciones
# def suma():
#     print("Ingrese un numero")
#     num1=int(input())
#     print("Ingrese otro numero")
#     num2=int(input())
#     print(num1+num2)
# def resta():
#     print("Ingrese un numero")
#     num1=int(input())
#     print("Ingrese otro numero")
#     num2=int(input())
#     print(num1-num2)
# def multi():
#     print("Ingrese un numero")
#     num1=int(input())
#     print("Ingrese otro numero")
#     num2=int(input())
#     print(num1*num2)
# def division():
#     print("Ingrese un numero")
#     num1=int(input())
#     print("Ingrese otro numero")
#     num2=int(input())
#     while num2==0:
#         print("Ingrese otro numero distinto de cero")
#         num2=int(input())
    
#     print(num1/num2)


# def cal():
#     while True:
#         print("Elija una operacion")
#         print("""
#         Suma=1
#         Resta=2
#         Multi=3
#         Division=4
#         Salir=5""")
#         op=int(input())
#         if op==(1):
#                 suma()
#         elif(op==(2)):
#                 resta()
#         elif(op==(3)):
#                 multi()
#         elif(op==(4)):
#                 division()
#         elif(op==(5)):
#                 break
#         else:
#                 print("Elija una opcion Valida")

# # cal()

# ruido=False
# while ruido!=True:
#     print("zzzzZZZZZZ")
#     print("*Susurra*  Hay ruido? si/no")
#     verifica=input()
#     if verifica=="si":
#       print("Ha despertado")
#       ruido=True
#     else:
#       print("siga durmiendo")
#https://github.com/diegoroblesrivera/FP3

import random


def dado():
    return random.randint(1,6)

def loto():
    return random.randint(1,38)

for i in range(6):
    print(loto())

# nom=dado()

# print(nom)