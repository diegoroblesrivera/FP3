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
# num=random.randint(0, 100)
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
#      0   1 2 3  4  5
# lista=[41,73,4,55,77,89]
# lista.append("Paola tiene " +str(lista[5])+ " años") # indice 6
# lista.append(True) #Indice 7
# if lista[7]:
#    lista.append(2.6) #indice 8
# for elemento in lista:
#     print(elemento)

# print(lista[-1])

##Insert ( agrerar elemento) Remove (Sacar Elemento)
#      0   1 2 3  4  5
lista=[41,73,4,55,77,89]
##lista.insert(3, "Sam")
lista.remove(55)
lista.sort()
lista.reverse()


for elemento in lista:
    
    print(elemento)



