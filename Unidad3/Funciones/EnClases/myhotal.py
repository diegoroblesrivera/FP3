hotel = [
    [[], [], [], [], [], [], ],#1 0
    [[], [], [], [], [], [], ],#2 1
    [[], [], [], [], [], [], ],#3 2
    [[], [], [], [], [], [], ],#4 3
    [[], [], [], [], [], [], ],#5 4
    [[], [], [], [], [], [], ],#6 5
    [[], [], [], [], [], [], ],#7 6
    [[], [], [], [], [], [], ],#8 7
    [[], [], [], [], [], [], ],#9 8
    [[], [], [], [], [], [], ],#10 9
]
while True:
    print("En que piso se va  alaojar?")
    piso=int(input())
    print("En que habitacion se va  alaojar?")
    hab=int(input())
    if hotel[piso-1][hab-1]:
        print("la habitacion esta usada\n")
    else:
        pasa=input("Ingrese el nombre del pasajero")
        hotel[piso-1][hab-1]={"nombre": pasa}
    
    
    
    for i in hotel:
        print(i)




