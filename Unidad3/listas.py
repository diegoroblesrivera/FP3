# Create : Crear
# Read : Leer
# Update : Actualizar
# Delete : Borar
##Listar una lista
#lista=[41,73,4,55,77,89]
import random
# for elemento in lista:
#     print(elemento)
##Mostrasr un elemento unico
# print(lista[1])

# ##Añadir un elemento a la lista
# num=random.randint(1, 99)
# num2=random.randint(0, 100)
# lista=[41,73,4,55,77,89]
# lista.append(num) 
# lista.append(num2)
# for elemento in lista:
#     print(elemento)


# bingo=[44,17,24,46,90]
# comodin=random.randint(10,99)

# while comodin in bingo:
#     #print("creando nuevo comodin")
#     comodin=random.randint(10,99)
# bingo.append(comodin)
# for num in bingo:
#     print(num)

##Añadir un elemento de otro tipo
# #       0  1 2 3  4  5
# lista=[41,73,4,55,77,89]
#     #  -6 -5 -4 -3 -2 -1
# # print(lista[4]+lista[2])

# lista.append("Paola tiene " +str(lista[2])+ " años") # indice 6
# lista.append(True) #Indice 7
# if lista[7]:
#    lista.append(2.6) #indice 8
# for elemento in lista:
#     print(elemento)

# print(lista[-1])

##Insert ( agrerar elemento) Remove (Sacar Elemento)
#      0   1 2 3  4  5
# lista=[41,73,4,55,77,89]
# ##lista.insert(3, "Sam")
# lista.remove(55)
# lista.sort()
# lista.reverse()


# for elemento in lista:
    
#     print(elemento)

# Hacer 1 matriz con 2 listas
# la primera lleva 3 nombres
# la segunda lleva 3 edades
# hacer print de los nombres y las edades correspondientes

# ej

# Su nombre es [nombre] y su edad es [edad]

matriz_sencilla = [
[1, 2, 3],
[4, 5, 6,66,55],
[7, 8, 9]
]

# print(matriz_sencilla[1][-1])


# for elemento in matriz_sencilla:
# 	print(elemento)

# for fila in matriz_sencilla:
# 	for elemento in fila:
# 		print(elemento, end=' ')

# bingo=[]


# for j in range(6):
#     num=random.randint(1, 99)
#     bingo.append(num)

# if len(bingo)<=5:
#     #crear un comodin
#     bingo.append(num)

# for i in bingo:
#     print(i)

# nombres=["Pedro pe", "Juan", "Diego", "Judas"]
# edades= []
# for j in range(len(nombres)):
#     num=random.randint(1, 99)
#     edades.append(num)

# for e in range(len(nombres)):
#     print("Su nombre es " ,nombres[e], " y su edad es ",str(edades[e]) )

# matriz_n=[[
#     ["Pedro pe", "Juan", "Diego", "Judas"],
#     [12,23,34,43]]
# ]

# for i in range(len(matriz_n[0][0])):
#     print(f"{matriz_n[0][0][i]} tiene {matriz_n[0][1][i]} años", end="\n")

matriz_n=[
    ["Pedro pe", "Juan", "Diego", "Judas"],
    [12,23,34,43],
    ["Arias", "Bravo", "Vargas", "Joo"]
]

# print(matriz_n[0][2], matriz_n[2][2], matriz_n[1][2] )

# print(matriz_n[0].index("Diego"))
nom=input("iNGRESE EL NOMBRE DE QUIN QUIERE SABER LA EDAD")

print(matriz_n[1][matriz_n[0].index(nom)])


