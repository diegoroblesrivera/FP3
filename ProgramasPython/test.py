# Entrada y Salida
# print("Por favor, ingresa tu nombre: ")
# nombre_usuario = input()
# print("Por favor, ingresa tu apellido: ")
# apellido=input()
# print("Hola, " + nombre_usuario + " "+apellido +"! Este es tu primer programa.") 

print("Por favor, ingresa un nuemro: ")
num1 = int(input())
print("Por favor, ingresa otro nuemro: ")
num2 = int(input())
print("Por favor, ingresa otro nuemro: ")
num3 = int(input())


if num1>num2 and num1>num3:
    print("El " + str(num1) + " Es mayor de todos")
elif num2>num3 :
    print("El " + str(num2) + " Es mayor de todos")
else:
    print("El " + str(num3) + " Es mayor de todos")

