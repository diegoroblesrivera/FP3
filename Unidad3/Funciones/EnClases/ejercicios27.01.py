# Caso 1: Nombre con Mayor Cantidad de Caracteres
# Escriban un programa en Python que permita a los usuarios 
# ingresar 3 nombres por panta-lla y almacenarlos en una lista.
# Luego, el programa debe determinar y mostrar el nombre que tiene
# la mayor cantidad de caracteres en un mensaje de salida por pantalla.

# nn=[]
# for k in range(3):
#     n=input("Ingrese un nombre")
#     nn.append(n)

# mas=max(nn,key=len)
# print("el nombre mas largo es", mas)

# Caso 2: Nombres y Apellidos Ordenados
# Creen dos listas, una para nombres y otra para apellidos.
# Almacenen 3 nombres y 3 apelli-dos en estas listas. Luego,
# muestren de forma ordenada los nombres y apellidos.

##Version Lista
# n=["Pedro", "juan", "Diego"]
# a=["Alfa", "kilo", "Beta"]

# for o in range(len(n)):
#     print(n[o], a[o])

##version diccionario
# nombres={"Diego":"Robles", "Juan": "Barrera", "Lila": "Becerra"}

# for key, valor in nombres.items():
#     print(f"{key} {valor}")
    
# Caso 3: Agregar Nombres y Eliminar el Menos Extenso
# Creen un programa que permita almacenar nombres en una lista. 
# El sistema debe preguntar si desean agregar otro nombre y seguir 
# permitiendo la entrada de nombres hasta que la respuesta sea "no".
# Después de ingresar n nombres, eliminen el nombre con la menor 
# cantidad de caracteres.

nomb=[]
resp=""
while resp!="no":
    resp=input("Desea ingresar un nombre ? (si /no)")
    if resp!="no":
        nn=input("Agrege el nombre")
        nomb.append(nn)
print(nomb)        
mini=min(nomb,key=len)
nomb.remove(mini)
print("El nombre eliminado fue", mini)
print(nomb) 