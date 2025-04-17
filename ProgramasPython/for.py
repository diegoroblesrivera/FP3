#conoceremos la estructura y uso de for

# for i in range(1,11):
#     print("Repetición numero ",i)

#ingrese un numero e imprima la tabla de ese numero

# num=int(input("Ingrese un numero"))

# for i in range(1,11):
#     print(num, "x",i, "=", num*i )


# for i in range(10,0,-1):
#     print(i )

# #pida un nombre al usuario y saludelo 3 veces

# nombre=input("Ingrese un nombre")

# for i in range(3):
#     print("Hola", nombre)

# #pida al usuario 3 notas y saque el prmedio
# #uso de for obligatorio
# suma=0
# for i in range(3):
#     n1=int(input("ingrese la nota "))
#     suma=suma+n1
# prom=suma/3
# print("El promedio es: ", round(prom))


# #pida al usuario ingresar la cantidad de notas
# # y saque el prmedio
# #uso de for obligatorio
# cant=int(input("ingrese la cantidad de notas "))
# suma=0
# for i in range(cant):
#     n1=int(input("ingrese la nota "))
#     suma=suma+n1
# prom=suma/cant
# print("El promedio es: ", round(prom))

cant=int(input("ingrese la cantidad de numeros "))
suma=0
for i in range(cant):
    n1=int(input("ingrese la nota "))
    suma+=n1
print("la suma de todos los numeros es ", suma)
