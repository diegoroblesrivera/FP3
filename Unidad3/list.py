# #      0 1  2  3 4 5          
# lista=[1,76,65,9, "lol",7,54]
# # #      -6 -5-4 -3-2-1

# # # print(lista)

# # # lista.append(3,"Mario")

# # # print(lista)

# # # # for i in lista:
# # #     print("Elemento ",i)

# # # while True:
    
# # #     print(lista)
# # #     m=int(input("Agregue u nuevo elemento"))
# # #     lista.append(m)
# # #     print(lista)
    
# # print(lista)

# # lista.insert(3,round(856.897))

# # print(lista)


# # print(lista)

# # lista.remove(76)

# # print(lista)

#  #      0           1      2
# lnom=["Pedro", "Juan", "Diego"]
# # ape=["Pascal", "Santaolaya", "Robles"]
# # car=["primer", "segundo", "tercer"]

# # for i in range(len(lnom)):
# #     print(" El", car[i], " nombre es ", lnom[i],ape[i])
    

# # print(lista)

# # lista.reverse()

# # print(lista)


# print(lnom)

# lnom.sort()

# print(lnom)

lnom=["Pedro", "Juan", "Diego"]
frutas=["uva", "melon", "melame", "pera", "fresa", "platano"]
pfru=[1300,1000,1500, 900, 1800, 1400]
c=1
car=[]
total=0

print("Quien va a comprar?")
for i in lnom:
    print(c,'.-',i)
    c+=1
sel=int(input())-1

# print(lnom[sel])

print("Bienvenido ",lnom[sel], "al la Fruteria" )

while len(car)<3:
    for fruta in range(len(frutas)):
        print(fruta+1, ".-", frutas[fruta])
    selfru=int(input("Selecciones una fruta"))-1
    print("Usted ha seleccionado ", frutas[selfru], "y su precio es", pfru[selfru] )
    car.append(selfru)
    print(car)
print("Verdureria Pelayos")
for i in car:
    print(f"",frutas[i],"......",  pfru[i])
    total=total+ pfru[i]

print("Su total fue ", total, "vuelva pronto ",lnom[sel])    

   
    