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

# matriz_sencilla = [
# [1, 2, 3],
# [4, 5, 6]
# ]

# print(matriz_sencilla[0][1])


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

nombres=["Pedro pe", "Juan", "Diego", "Judas"]
edades= []
for j in range(len(nombres)):
    num=random.randint(1, 99)
    edades.append(num)

for e in range(len(nombres)):
    print("Su nombre es " ,nombres[e], " y su edad es ",str(edades[e]) )




